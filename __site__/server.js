const express = require('express');
const fs = require('fs');
const path = require('path');
const marked = require('marked');

const app = express();
const CONTENT_ROOT = path.join(__dirname, '..');
const TRAINING_FOLDERS = [
  'ansible', 'aws', 'container_tech', 'docker', 'devops', 'git', 'grafana', 'jenkins', 'kubernetes', 'linux', 'loki', 'minikube', 'monitoring', 'prometheus', 'python', 'terraform', 'vault'
];

app.use(express.static(path.join(__dirname, 'public')));

// Helper to get directory listing
function getDirTree(dir, base = '') {
  const result = [];
  fs.readdirSync(dir).forEach(file => {
    // Only show folders in TRAINING_FOLDERS at root level
    if (base === '' && !TRAINING_FOLDERS.includes(file)) return;
    if (file.startsWith('.') || file === '__site__') return; // Ignore hidden/system folders
    const absPath = path.join(dir, file);
    const relPath = path.join(base, file);
    const stat = fs.statSync(absPath);
    if (stat.isDirectory()) {
      // Only include subfolders if they contain .md files or subfolders with .md files
      const children = getDirTree(absPath, relPath);
      if (children.length > 0) {
        result.push({
          type: 'dir',
          name: file,
          path: relPath,
          children
        });
      }
    } else if (file.endsWith('.md')) {
      result.push({
        type: 'file',
        name: file,
        path: relPath
      });
    }
  });
  return result;
}

app.get('/', (req, res) => {
  const tree = getDirTree(CONTENT_ROOT);
  res.send(`<!DOCTYPE html>
<html>
<head>
  <title>DevOps Training Browser</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  <style>body{padding:2rem;} .tree{font-size:1.1rem;} .md-content{margin-top:2rem;}</style>
</head>
<body>
  <h1>DevOps Training Content</h1>
  <div class="row">
    <div class="col-md-4">
      <h4>Browse Files</h4>
      <div class="tree" id="tree"></div>
    </div>
    <div class="col-md-8">
      <div class="md-content" id="md-content">Select a Markdown file to view.</div>
    </div>
  </div>
  <script>
    const tree = JSON.parse(decodeURIComponent("${encodeURIComponent(JSON.stringify(tree))}"));
    function renderTree(nodes, parent) {
      nodes.forEach(function(node) {
        var el = document.createElement('div');
        if(node.type === 'dir') {
          el.innerHTML = '<b>[Folder] ' + node.name + '</b>';
          el.style.marginLeft = '1em';
          parent.appendChild(el);
          renderTree(node.children, el);
        } else {
          el.innerHTML = '<a href="#" onclick="loadMD(\'' + node.path.replace(/'/g, "\\'") + '\')">[File] ' + node.name + '</a>';
          el.style.marginLeft = '2em';
          parent.appendChild(el);
        }
      });
    }
    renderTree(tree, document.getElementById('tree'));
    async function loadMD(mdPath) {
      const resp = await fetch('/md?path=' + encodeURIComponent(mdPath));
      const html = await resp.text();
      document.getElementById('md-content').innerHTML = html;
    }
  </script>
</body>
</html>`);
});

app.get('/md', (req, res) => {
  const relPath = req.query.path;
  if (!relPath || relPath.includes('..')) return res.status(400).send('Invalid path');
  const absPath = path.join(CONTENT_ROOT, relPath);
  if (!fs.existsSync(absPath) || !absPath.endsWith('.md')) return res.status(404).send('File not found');
  const md = fs.readFileSync(absPath, 'utf8');
  res.send(marked.parse(md));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`DevOps Training Browser running at http://localhost:${PORT}`);
});
