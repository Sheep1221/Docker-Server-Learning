from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)


# MongoDB connect
client = MongoClient('mongodb://mongodb:27017/')
db = client.mydatabase # Use your database name
collection = db.user_inputs # User your collection name

mydb = client["yukai_test1"]
mycol = mydb["myself"]


# Sample data for test api
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"}
]

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/admin")
def admin_page():
    return "<h1>This is the Admin Page</h1>"

# I/O and MongoDB
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

# test api

## Get method
@app.route('/test_api/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((tmp_item for tmp_item in items if tmp_item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error":"item not found"}), 404


## Get for MongoDB
@app.route('/test_api/<name>', methods=['GET'])
def get_item_by_name(name):
    item = mycol.find_one({"name": name}, {'_id': 0})
    if item:
        return jsonify(item)
    return jsonify({"error":"item not found"}), 404


if __name__ == "__main__":
    app.run(port=3333, host="0.0.0.0")
