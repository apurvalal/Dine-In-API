from email import message
import json
from flask import Flask, request, jsonify;
from flask_pymongo import PyMongo;
from bson.objectid import ObjectId;
from bson import json_util;
import socket;
import random;
from supermind.services.menu_service import MenuService;

# Customer sends order to server [POST]. Server stores order in database [GET].
# Customer asks for the bill [GET]. Server returns bill. 
# Server deletes the order from active orders table.

app = Flask(__name__);
app.config['MONGO_URI'] = 'mongodb://localhost:27017/dev';
mongo = PyMongo(app);
db = mongo.db;

def parse_json(data):
    return json.loads(json_util.dumps(data))

@app.route("/")
def index():
    hostname = socket.gethostname();
    return jsonify(message="Hello from {}".format(hostname));

@app.route("/token")
def get_token():
    random_token = random.randint(0, 100);
    token = db.tokens.find_one({'token': random_token});

    if token is None:
        token = {'token': random_token};
        db.tokens.insert_one(token);
    
    return jsonify(token=token['token']);

@app.route("/api/order", methods=["POST"])
def add_order():
    token = request.json["token"];
    items = request.json["items"];
    order = db.orders.find_one({"token": token}); 
    if order is None:
        order = db.orders.insert_one({"token": token, "items": items});
    else:
        for key,value in items.items():
            if key in order["items"]:
                order["items"][key] += value;
            else:
                order['items'][key] = value;
        
        db.orders.update_one({"token": token}, {"$set": {"items": order['items']}});
    return jsonify("Order added");

@app.route("/api/order/<token>", methods=["GET"])
def get_order(token):
    order = db.orders.find_one({"token": int(token)});

    print(order);
    if order is None:
        return jsonify(message="Order not found"), 404;
    else:
        items = order["items"];
        indian = MenuService().getIndian();
        chinese = MenuService().getChinese();
        continental = MenuService().getContinental();

        total = 0;
        item_amount = "";
        amount = {};
        for key,value in items.items():
            if key in indian:
                total += indian[key] * value;
                item_amount = "{} x {} = {}".format(indian[key], value, indian[key] * value);
                amount[key] = item_amount;

            elif key in chinese:
                total += chinese[key] * value;
                item_amount = "{} x {} = {}".format(chinese[key], value, chinese[key] * value);
                amount[key] = item_amount;

            elif key in continental:
                total += continental[key] * value;
                item_amount = "{} x {} = {}".format(continental[key], value, continental[key] * value);
                amount[key] = item_amount;
    
        bill = {'token':token, 'total': total, 'items': amount};
    return jsonify(bill);

@app.route("/api/order/<order_id>/bill", methods=["POST"])
def add_bill(order_id):
    bill_id = request.json["bill_id"];
    bill = db.bills.find_one({"bill_id": bill_id});
    if bill is None:    # bill not found
        bill = db.bills.insert_one({"bill_id": bill_id});
    return jsonify(bill_id=bill_id);

@app.route("/api/menu/continental", methods=["POST"])
def add_continental_item():
    item_name = request.json["item_name"];
    item_price = request.json["price"];
    menu = db.menus.continental.find_one({"item_name": item_name});
    if menu is None:
        menu = db.menus.continental.insert_one({"item_name": item_name, "item_price": item_price});
    return jsonify(item_name=item_name);

@app.route("/api/menu/indian", methods=["POST"])
def add_indian_item():
    item_name = request.json["item_name"];
    item_price = request.json["price"];
    menu = db.menus.indian.find_one({"item_name": item_name});
    if menu is None:
        menu = db.menus.indian.insert_one({"item_name": item_name, "item_price": item_price});
    return jsonify(item_name=item_name);

@app.route("/api/menu/chinese", methods=["POST"])
def add_chinese_item():
    item_name = request.json["item_name"];
    item_price = request.json["price"];
    menu = db.menus.chinese.find_one({"item_name": item_name});
    if menu is None:
        menu = db.menus.chinese.insert_one({"item_name": item_name, "item_price": item_price});
    return jsonify(item_name=item_name);

@app.route("/api/menu/continental", methods=["GET"])
def get_continental():
    menu = MenuService();
    continental_menu = menu.getContinental();
    continental_menu = parse_json(continental_menu)

    return jsonify(continental_menu)

@app.route("/api/menu/indian", methods=["GET"])
def get_indian():
    menu = MenuService();
    indian_menu = menu.getIndian();
    indian_menu = parse_json(indian_menu)

    return jsonify(indian_menu)

@app.route("/api/menu/chinese", methods=["GET"])
def get_chinese():
    menu = MenuService();
    chinese_menu = menu.getChinese();
    chinese_menu = parse_json(chinese_menu)

    return jsonify(chinese_menu)

if __name__ == "__main__":
    app.run(debug=True)