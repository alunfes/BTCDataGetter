import websocket
import threading
import time

testi = 1

class BtcFxDataGetter:
    varx = 1

    def __init__(self):
        self.thread = threading.Thread(target=self.testA, args=())
        self.thread.daemon = True  # Daemonize thread
        self.thread.start()
        self.thread.join()

    def connection(self):


    def testA(self):
        while True:
            print(self.varx)
            self.varx+=1
            time.sleep(1)

    def testB(self):
        self.b = "testb"
        print(self.b)


bfd = BtcFxDataGetter()
#bfd.testA()
#bfd.testB()


class websocketConnection:
    executions_url = "lightning_executions_"
    def getExecutionsConnection(self,
                      ):