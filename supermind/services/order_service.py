from supermind.models.order import Order
from supermind.services.order_service_interface import OrderServiceInterface
import datetime

class OrderService(OrderServiceInterface):
    def addOrder(self, order_id):
        order = Order()
        order.setOrderId(order_id)
        order.setItems(self.getItems(order_id))
        order.setCreatedAt(datetime.now())
        order.setUpdatedAt(datetime.now())
        return order