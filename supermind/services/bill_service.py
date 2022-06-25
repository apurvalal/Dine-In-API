import datetime
from supermind.models.bill import Bill
from supermind.services.bill_service_interface import BillServiceInterface

class BillService(BillServiceInterface):
    bill_details = {}
    def addBill(self, bill_id):
        bill = Bill()
        bill.setBillId(bill_id)
        bill.setItems(self.getItems(bill_id))
        bill.setCreatedAt(datetime.now())
        bill.setUpdatedAt(datetime.now())
        
        self.__class__.bill_details[bill_id] = bill
        return bill
