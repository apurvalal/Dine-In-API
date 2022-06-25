from email import message
import json
from flask import Flask, request, jsonify;
from flask_pymongo import PyMongo;
from bson.objectid import ObjectId;
from bson import json_util
import socket;

# Customer sends order to server [POST]. Server stores order in database [GET].
# Customer asks for the bill [GET]. Server returns bill. 
# Server deletes the order from active orders table.

app = Flask(__name__);
app.config['MONGO_URI'] = 'mongodb://localhost:27017/dev';
mongo = PyMongo(app);
db = mongo.db;

@app.route("/")
def index():
    hostname = socket.gethostname();
    return jsonify(message="Hello from {}".format(hostname));

@app.route("/api/order", methods=["POST"])
def add_order():
    order_id = request.json["order_id"];
    order = db.orders.find_one({"order_id": order_id}); 
    if order is None:
        order = db.orders.insert_one({"order_id": order_id});
    return jsonify(order_id=order_id);

@app.route("/api/order/<order_id>", methods=["GET"])
def get_order(order_id):
    print(order_id);
    order = db.orders.find_one({"order_id": int(order_id)});

    print(order);
    if order is None:
        return jsonify(message="Order not found"), 404;
    return json.loads(json_util.dumps(order));

@app.route("/api/order/<order_id>/bill", methods=["POST"])
def add_bill(order_id):
    bill_id = request.json["bill_id"];
    bill = db.bills.find_one({"bill_id": bill_id});
    if bill is None:    # bill not found
        bill = db.bills.insert_one({"bill_id": bill_id});
    return jsonify(bill_id=bill_id);

if __name__ == "__main__":
    app.run(debug=True)