import json
import pandas as pd

class MenuService():
    # Initialize the menu service
    def __init__(self):
        self.indian = pd.read_csv('src/data/indian.csv')    # Read the indian menu from the CSV file
        self.chinese = pd.read_csv('src/data/chinese.csv')  # Read the chinese menu from the CSV file
        self.continental = pd.read_csv('src/data/continental.csv')  # Read the continental menu from the CSV file

    # Get the indian menu
    def getIndian(self):
        raw_menu = self.indian.to_json(orient='records')  # Convert the data to JSON
        raw_menu = json.loads(raw_menu) # Parse the data as JSON

        final_menu = {} # Create a new dictionary
        for item in raw_menu:   # For each item in the menu
            final_menu[item['item_name']] = item['item_price']  # Add the item to the dictionary
        return final_menu

    # Get the chinese menu
    def getChinese(self):
        raw_menu = self.chinese.to_json(orient='records')
        raw_menu = json.loads(raw_menu)

        final_menu = {}
        for item in raw_menu:
            final_menu[item['item_name']] = item['item_price']
        return final_menu

    # Get the continental menu
    def getContinental(self):
        raw_menu = self.continental.to_json(orient='records')
        raw_menu = json.loads(raw_menu)

        final_menu = {}
        for item in raw_menu:
            final_menu[item['item_name']] = item['item_price']
        return final_menu

    # Add an item to the indian menu
    def addIndianItem(self, item_name, item_price):
        # Add the item to the menu
        self.indian = self.indian.append({'item_name': item_name, 'item_price': item_price}, ignore_index=True)
        self.indian.to_csv('src/data/indian.csv', index=False)  # Write the menu to the CSV file

    # Add an item to the chinese menu
    def addChineseItem(self, item_name, item_price):
        self.chinese = self.chinese.append({'item_name': item_name, 'item_price': item_price}, ignore_index=True)
        self.chinese.to_csv('src/data/chinese.csv', index=False)

    # Add an item to the continental menu
    def addContinentalItem(self, item_name, item_price):
        self.continental = self.continental.append({'item_name': item_name, 'item_price': item_price}, ignore_index=True)
        self.continental.to_csv('src/data/continental.csv', index=False)