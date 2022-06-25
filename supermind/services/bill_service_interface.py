import abc

class BillServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addBill(self, bill_id):
        pass


