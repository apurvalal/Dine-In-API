from email import message
import json
from flask import Flask, request, jsonify;
from flask_pymongo import PyMongo;
from bson.objectid import ObjectId;
from bson import json_util;
import socket;
import random;
from src.services.menu_service import MenuService;

app = Flask(__name__);
app.config['MONGO_URI'] = 'mongodb://localhost:27017/dev'; # Change this to your MongoDB URI
mongo = PyMongo(app); # Create a PyMongo instance
db = mongo.db;

# Parse the data as JSON
def parse_json(data):
    return json.loads(json_util.dumps(data))

# Generate a token for the user
@app.route("/token")
def add_token():
    # Check if the token is in the database
    isAdded = False;

    while not isAdded: 
        random_token = random.randint(0, 100); # Generate a random token
        token = db.tokens.find_one({'token': random_token}); # Check if the token is already in the database

        if token is None: # If the token is not in the database, add it
            token = {'token': random_token};
            db.tokens.insert_one(token);
            isAdded = True;
        # If the token is in the database, generate a new token
    return jsonify(token=token['token']);

# Add an order to the database
@app.route("/api/order", methods=["POST"])
def add_order():    
    token = request.json["token"];
    items = request.json["items"];
    
    # Check if the token is in the database
    # If the token is not in the database, return an error
    if db.tokens.find_one({'token': token}) is None:
        return jsonify(message="Invalid token"), 401;
    
    order = db.orders.find_one({"token": token});
    
    # If the token is in the database, but the order is not in the database, add the order
    if order is None:
        order = db.orders.insert_one({"token": token, "items": items});
    # If the token is in the database, and the order is in the database, update the order
    else:
        for key,value in items.items():
            # If the item is already in the order, update the quantity
            if key in order["items"]:
                order["items"][key] += value;   # Add the new items to the order
            else:
                order['items'][key] = value;
        
        db.orders.update_one({"token": token}, {"$set": {"items": order['items']}}); # Update the order
    return jsonify("Order added");

# Get all the orders
@app.route("/api/order", methods=["GET"])
def get_all_orders():
    orders = db.orders.find();
    orders = parse_json(orders);    # Parse the data as JSON
    return jsonify(orders);

# Get the bill with the given token
@app.route("/api/order/<token>", methods=["GET"])
def get_order(token):
    order = db.orders.find_one({"token": int(token)}); 

    # If the token is not in the database, return an error
    if order is None:
        return jsonify(message="Order not found"), 404;
    else:
        items = order["items"]; # Get the items in the order

        # Get the menus from the database
        indian = MenuService().getIndian();
        chinese = MenuService().getChinese();   
        continental = MenuService().getContinental();

        total = 0;  # Calculate the total price of the order
        item_amount = "";   # Create a string with the items and their quantities
        amount = {};    # Create a dictionary to display the items and their quantities

        # Loop through the items in the order
        for key,value in items.items():
            # If the item is in any menu, add the price to the total price
            if key in indian:
                total += indian[key] * value;   # Add the price of the item to the total
                item_amount = "{} x {} = {}".format(indian[key], value, indian[key] * value); # Create a string with the item and its quantity
                amount[key] = item_amount;  # Add the item and its quantity to the dictionary

            elif key in chinese:
                total += chinese[key] * value;
                item_amount = "{} x {} = {}".format(chinese[key], value, chinese[key] * value);
                amount[key] = item_amount; 

            elif key in continental:
                total += continental[key] * value;
                item_amount = "{} x {} = {}".format(continental[key], value, continental[key] * value);
                amount[key] = item_amount;  
    
        bill = {'token':token, 'total': total, 'items': amount};    # Create a dictionary with the bill
    return jsonify(bill);

# Delete the order with the given token
@app.route("/api/order/<token>", methods=["DELETE"])
def delete_order(token):
    # Check if the token is in the database. If the token is not in the database, return an error
    if db.orders.find_one({"token": int(token)}) is None:
        return jsonify(message="Order not found"), 404;

    db.tokens.delete_one({"token": int(token)});    # Delete the token
    db.orders.delete_one({"token": int(token)});    # Delete the order
    return jsonify(message="Order deleted");

# Add a new item to the continental menu
@app.route("/api/menu/continental", methods=["POST"])
def add_continental_item():
    menu = MenuService();   # Create a new menu service
    menu.addContinentalItem(request.json["item_name"], request.json["item_price"]); # Add the item to the menu

    return jsonify("Item added");

# Add a new item to the indian menu
@app.route("/api/menu/indian", methods=["POST"])
def add_indian_item():
    menu = MenuService();   # Create a new menu service
    menu.addIndianItem(request.json["item_name"], request.json["price"]);   # Add the item to the menu

    return jsonify("Item added");

# Add a new item to the chinese menu
@app.route("/api/menu/chinese", methods=["POST"])
def add_chinese_item():
    menu = MenuService();   # Create a new menu service
    menu.addChineseItem(request.json["item_name"], request.json["price"]);  # Add the item to the menu

    return jsonify("Item added");

# Get the continental menu
@app.route("/api/menu/continental", methods=["GET"])
def get_continental():
    menu = MenuService();   # Create a new menu service
    continental_menu = menu.getContinental();   # Get the menu
    continental_menu = parse_json(continental_menu) # Parse the data as JSON

    return jsonify(continental_menu)

# Get the indian menu
@app.route("/api/menu/indian", methods=["GET"])
def get_indian():
    menu = MenuService();   # Create a new menu service
    indian_menu = menu.getIndian();  # Get the menu
    indian_menu = parse_json(indian_menu)   # Parse the data as JSON

    return jsonify(indian_menu)

# Get the chinese menu
@app.route("/api/menu/chinese", methods=["GET"])
def get_chinese():
    menu = MenuService();   # Create a new menu service
    chinese_menu = menu.getChinese();   # Get the menu
    chinese_menu = parse_json(chinese_menu) # Parse the data as JSON

    return jsonify(chinese_menu)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)