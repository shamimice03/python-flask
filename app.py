from flask import Flask, request
import jsonify

app = Flask(__name__)
stores = [
    {
        "name": "My Store", 
        "items": [
            {
            "name": "My Item", 
            "price": 15.99
            }
        ]
    }
]

@app.get('/store')
def get_stores():
    return stores

@app.post('/store')
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return new_store, 201

@app.post('/store/<string:name>/items')
def create_item_in_store(name):
    request_data = request.get_json()
    print(request_data)
    for store in stores:
        if store["name"] == name:
            for item in request_data:
                new_item = {
                    "name": item["name"],
                    "price": item["price"]
                }
                store["items"].append(new_item)
            return store, 201
    return {"message": "Store not found"}, 404

@app.get('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404

@app.get('/store/<string:name>/items')
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            return store["items"]
    return {"message": "Store not found"}, 404