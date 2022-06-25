class Bill(object):
    def __init__(self):
        self.id = None
        self.bill_id = None
        self.items = {}
        self.total_price = 0
        self.created_at = None
        self.updated_at = None

    def setId(self, id):
        self.id = id
    
    def getId(self):
        return self.id
    
    def setBillId(self, bill_id):
        self.bill_id = bill_id

    def getBillId(self):
        return self.bill_id

    def setItems(self, items):
        self.items = items

    def getItems(self):
        return self.items

    def setTotalPrice(self, total_price):
        self.total_price = total_price

    def getTotalPrice(self):
        return self.total_price

    def setCreatedAt(self, created_at):
        self.created_at = created_at

    def getCreatedAt(self):
        return self.created_at

    def setUpdatedAt(self, updated_at):
        self.updated_at = updated_at

    def getUpdatedAt(self):
        return self.updated_at