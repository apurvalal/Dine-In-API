import json
import pandas as pd

class MenuService():
    def __init__(self):
        self.indian = pd.read_csv('supermind/data/menu/indian.csv')
        self.chinese = pd.read_csv('supermind/data/menu/chinese.csv')
        self.continental = pd.read_csv('supermind/data/menu/continental.csv')

    def getIndian(self):
        raw_menu = self.indian.to_json(orient='records')
        raw_menu = json.loads(raw_menu)

        final_menu = {}
        for item in raw_menu:
            final_menu[item['item_name']] = item['item_price']
        return final_menu

    def getChinese(self):
        raw_menu = self.chinese.to_json(orient='records')
        raw_menu = json.loads(raw_menu)

        final_menu = {}
        for item in raw_menu:
            final_menu[item['item_name']] = item['item_price']
        return final_menu

    def getContinental(self):
        raw_menu = self.continental.to_json(orient='records')
        raw_menu = json.loads(raw_menu)

        final_menu = {}
        for item in raw_menu:
            final_menu[item['item_name']] = item['item_price']
        return final_menu