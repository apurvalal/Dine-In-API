import abc

class OrderServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addOrder(self, order_id):
        pass