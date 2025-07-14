Create a simple Flask web app.

Write a Dockerfile to containerize the app.

Build a Docker image from it.

Run the container and test it in a browser.

Use a volume to persist data.

Use Docker networking to connect two containers.

*** How to create flask Application ***

```python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Dockerized Flask!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

```

## requirements.txt file 

Flask==2.2.5
