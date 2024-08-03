from flask import Flask, render_template, request
from pymongo import MongoClient
import os

app = Flask(__name__)


# MongoDB connect
client = MongoClient('mongodb://mongodb:27017/')
db = client.mydatabase # Use your database name
collection = db.user_inputs # User your collection name

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/admin")
def admin_page():
    return "<h1>This is the Admin Page</h1>"

@app.route('/testIO', methods=['GET', 'POST'])
def test_io():
    if request.method == 'POST':
        try:
            user_input = request.form['user_input']

            # Store the input into MongoDB
            data = {'user_input': user_input}
            result = collection.insert_one(data)

            # return insert ID and show on html
            return render_template('index.html', user_input=user_input)
        except KeyError:
            return "Error: 'user_input' not found in form data", 400
    return render_template('index.html', user_input=None)

if __name__ == "__main__":
    app.run(port=3333, host="0.0.0.0")
