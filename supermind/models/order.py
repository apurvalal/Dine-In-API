class Order(object):
    def __init__(self):
        self.id = None
        self.order_id = None
        self.items = {}
        self.created_at = None
        self.updated_at = None

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setOrderId(self, order_id):
        self.order_id = order_id

    def getOrderId(self):
        return self.order_id

    def setItems(self, items):
        self.items = items

    def getItems(self):
        return self.items

    def setCreatedAt(self, created_at):
        self.created_at = created_at

    def getCreatedAt(self):
        return self.created_at

    def setUpdatedAt(self, updated_at):
        self.updated_at = updated_at

    def getUpdatedAt(self):
        return self.updated_at


    