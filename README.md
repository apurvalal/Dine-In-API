# Dine In API

## About

This is a simple API for a restaurant called Dine In.
It is built on top of the Flask framework in Python.
The aim of this API is to provide a simple way to manage orders.

## Tools Used

- Flask: The web framework used for this project.
- MongoDB: The database used for this project.
- PyMongo: Used for interacting with the database.
- JSON: Used for parsing JSON.
- Random: Used for generating random tokens.
- JSON Utilities
- Postman: Used for testing the API.

## Dependencies

- Flask: `pip install flask`
- PyMongo: `pip install pymongo`
- JSON: `pip install json`
- JSON Utilities: `pip install jsonutils`

## Running the project

- Make sure you have the dependencies installed.
- Make sure you have the database running.
- Run the project: python app.py
- Open Postman: http://localhost:5000/

## Structure

- The customer can request to view the items in the menu by selecting a mode: Continental, Indian or Chinese
- Server responds with the items in the menu along with the prices
- The customer can then send the items they want to order along with the quantity
- Server stores the order in an orders table
- The customer can then request for bill after having their meal
- Server responds with the total price of the order in the form of a bill
- The order can then be removed from the orders table

## Endpoints
- /api/token: Generates a random token and adds it to the database
- [POST] /api/order: Adds an order to the database
- [GET] /api/order: Returns all the orders in the database
- [GET] /api/order/<token>: Returns the bill for the order with the given token
- [DELETE] /api/order/<token>: Removes the order with the given token from the database
- [POST] /api/menu/continental: Adds an item to the continental menu
- [POST] /api/menu/indian: Adds an item to the indian menu
- [POST] /api/menu/chinese: Adds an item to the chinese menu
- [GET] /api/menu/continental: Returns the continental menu
- [GET] /api/menu/indian: Returns the indian menu
- [GET] /api/menu/chinese: Returns the chinese menu
