#https://note.mu/yuza_cc/n/n6fb257a745c8

import websocket
import threading
import time
import json
import sqlite3
from config import *
import BTCData


class BtcFxDataGetter:
    varx = 1

    def __init__(self, channel, symbol):
        self.symbol = symbol
        self.ticker = None
        self.channel = channel
        self.connect()

    def connect(self):
        self.ws = websocket.WebSocketApp(
            'wss://ws.lightstream.bitflyer.com/json-rpc', header=None,
            on_open = self.on_open, on_message = self.on_message,
            on_error = self.on_error, on_close = self.on_close)
        self.ws.keep_running = True 
        websocket.enableTrace(True)
        self.thread = threading.Thread(target=lambda: self.ws.run_forever())
        self.thread.daemon = True
        self.thread.start()

    def is_connected(self):
        return self.ws.sock and self.ws.sock.connected

    def disconnect(self):
        print('disconnected')
        self.ws.keep_running = False
        self.ws.close()

    def get(self):
        return self.ticker

    def on_message(self, ws, message):
        message = json.loads(message)['params']
        self.ticker = message['message']
        if self.ticker is not None:
            BTCData.BTCExecutionData.addExecution(dict(self.ticker[0]))

    def on_error(self, ws, error):
        print('error')
        self.disconnect()
        time.sleep(3)
        self.connect()

    def on_close(self, ws):
        print('Websocket disconnected')

    def on_open(self, ws):
        ws.send(json.dumps( {'method':'subscribe',
            'params':{'channel':self.channel + self.symbol}} ))
        time.sleep(1)
        print('Websocket connected')

    #def createDB():
    #    con = sqlite3.connect('FXBTC.db')
    #    cursor = con.cursor()
    #    cursor.executescript("""DROP TABLE IF EXISTS executions;CREATE TABLE executions(id, side, price, size, exec_date, buy_id, sell_id)""")
        #cursor.execute("CREATE TABLE executions(id, side, price, size, exec_date, buy_id, sell_id)")






if __name__ == '__main__':

    bfd = BtcFxDataGetter('lightning_executions_','FX_BTC_JPY')
    num_failed = 0

    while bfd.is_connected() != True or num_failed < 10: 
         time.sleep(1)
         print('connecting...', bfd.is_connected())
         num_failed +=1
         if(bfd.is_connected()==True):
             while True:
                print(bfd.get())
                data = bfd.get()
                if data is not None:
                    side = data[0]['side']
                    price = data[0]['price']
                    size = data[0]['size']

                    print('side={}, price={}, size={}'.format(side, price, size))
                #time.sleep(0.5)
    bfd.disconnect()
    self.thread.close()


    """ bfd = BtcFxDataGetter('lightning_ticker_','FX_BTC_JPY')
    num_failed = 0

    while bfd.is_connected() != True or num_failed < 10: 
         time.sleep(1)
         print('connecting...', bfd.is_connected())
         num_failed +=1
         if(bfd.is_connected()==True):
             while True:
                print(bfd.get())
                data = bfd.get()
                if data is not None:
                    bid = data['best_bid']
                    ask = data['best_ask']
                    spread = ask - bid
                    print('spread={}, ask={}, bid={}'.format(spread,ask,bid))
                time.sleep(0.5)
    bfd.disconnect()
    self.thread.close() """


else:
    print('called as a module')