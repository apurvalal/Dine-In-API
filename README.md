# Dine In API

## Tools Used

- Flask
- MongoDB

## Structure

- The customer can request for items in the menu by selecting a mode: Continental, Indian or Chinese
- Server responds with the items in the menu along with the prices
- The customer can then send the items they want to order along with the quantity
- Server stores the order in active orders table
- The customer can then request for bill after having their meal
- Server responds with the total amount of the order in the form of a bill
- Server removes the order from active orders table
