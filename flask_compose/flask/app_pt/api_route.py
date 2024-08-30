from flask import jsonify

def init_api_routes(app):
    mycol = app.mycol
    
    ## Get one
    @app.route('/PT_family/api/<name>', methods=['GET'])
    def get_item_by_name(name):
        item = mycol.find_one({"name": name}, {'_id': 0})
        if item:
            return jsonify(item)
        return jsonify({"error": "item not found"}), 404

    ## Get all
    @app.route('/PT_family/api', methods=['GET'])
    def get_all_item():
        items = list(mycol.find({}, {'_id': 0})) # json not able to show id
        return jsonify(items)

    ## Add into MongoDB 
    @app.route('/PT_family/api', methods=['POST'])
    def add_item():
        item = request.json
        mycol.insert_one(item)
        return jsonify({"message": "Item added successfully"}), 201

    ## Extend existed item
    @app.route('/PT_family/api/<name>', methods=['PATCH'])
    def extend_item(name):
        existed = mycol.find_one({"name": name}, {'_id': 0})
        print("exist = ", existed)
        if existed:
            item = request.json
            mycol.update_one({"name": name}, {"$set": item})
            return jsonify({"message": "Item updated successfully"}), 201
        return jsonify({"message": "<name> not found"}), 404

    ## Delete from MongoDB
    @app.route('/PT_family/api/<name>', methods=['DELETE'])
    def delete_item(name):
        result = mycol.delete_one({"name": name})
        if result.deleted_count == 0:
            return jsonify({"message": "<name> not found"}), 404
        return jsonify({"message": "<name> deleted successfully"}), 201