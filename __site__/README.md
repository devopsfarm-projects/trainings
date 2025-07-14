# DevOps Training Static Site
> ⚠️ **Work In Progress:** This site is actively being developed. Features and content may change frequently.
This static site lets you browse and view all Markdown content from your DevOps training workspace, and includes a whiteboard tool for diagrams and flowcharts.

## Getting Started

1. **Install dependencies**
   ```bash
   cd __site__
   npm install
   ```

2. **Start the server**
   ```bash
   npm start
   ```

3. **Open in browser**
   Go to [http://localhost:3000](http://localhost:3000) to browse your content and use the whiteboard.

## Features
- Browse all folders and Markdown files in your workspace
- Render Markdown files as HTML
- Responsive, modern UI (Bootstrap)
- Whiteboard tool for drawing and flowcharts (`/public/whiteboard.html`)

## Deployment
You can deploy this site on any platform that supports Node.js (e.g., Vercel, Heroku, DigitalOcean, AWS EC2).

- For production, set the `PORT` environment variable as needed.
- Make sure your workspace content is accessible to the server.

## Customization
- Add logos or images to `/public` and reference them in your site as needed.
- To add more features, edit `server.js` and static files in `/public`.

---
Made with ❤️ for DevOps learners.
