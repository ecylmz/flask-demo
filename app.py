import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.environ.get("NAME", "Default")
    return f"Hello, {name}. Welcome to the CI/CD World!1"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
