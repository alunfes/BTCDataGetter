import threading

class BTCExecutionData:
    lock = threading.Lock()
    id = []
    side = []
    price = []
    size = []
    exec_date = []
    buy_child_order_acceptance_id = []
    sell_child_order_acceptance_id = []

    @classmethod
    def initialize(self):
        self.lock = threading.Lock()
        self.id = []
        self.side = []
        self.price = []
        self.size = []
        self.exec_date = []
        self.buy_child_order_acceptance_id = []
        self.sell_child_order_acceptance_id = []
    
    @classmethod
    def addExecution(data, self):
        with lock.acquire:
            self.id.append(data['id'])
            self.side.append(data['side'])
            self.price.append(data['price'])
            self.size.append(data['size'])
            self.exec_date.append(data['exec_date'])
            self.buy_child_order_acceptance_id.append(data['buy_child_order_acceptance_id'])
            self.sell_child_order_acceptance_id.append(data['sell_child_order_acceptance_id'])
    
    @classmethod
    def getFirstData(self):
        with lock.acquire:
            return [self.id.pop(0) self.side.pop(0), self.price.pop(0), self.size.pop(0), self.exec_date.pop(0), self.buy_child_order_acceptance_id.pop(0), self.sell_child_order_acceptance_id.pop(0)]


    @classmethod
    def getAllExecutions(self):
        with lock.acquire:
            res = {self.id, self.side, self.price, self.size, self.exec_date,self.buy_child_order_acceptance_id,self.sell_child_order_acceptance_id}
            initialize()
            return res

