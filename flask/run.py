from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/admin")
def admin_page():
    return "<h1>This is the Admin Page</h1>"

if __name__ == "__main__":
    app.run(port=3333, host="0.0.0.0")
