#https://note.mu/yuza_cc/n/n6fb257a745c8

import websocket
import threading
import time
import json
from config import *


class BtcFxDataGetter:
    varx = 1

    def __init__(self, symbol):
        self.symbol = symbol
        self.ticker = None
        self.connect()

    def connect(self):
        self.ws = websocket.WebSocketApp(
            'wss://ws.lightstream.bitflyer.com/json-rpc', header=None,
            on_open = self.on_open, on_message = self.on_message,
            on_error = self.on_error, on_close = self.on_close)
        self.ws.keep_running = True 
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

    def on_error(self, ws, error):
        print('error')
        self.disconnect()
        time.sleep(3)
        self.connect()

    def on_close(self, ws):
        print('Websocket disconnected')

    def on_open(self, ws):
        ws.send(json.dumps( {'method':'subscribe',
            'params':{'channel':'lightning_ticker_' + self.symbol}} ))
        time.sleep(1)
        print('Websocket connected')



if __name__ == '__main__':
    print('kita')
    thread = BtcFxDataGetter('FX_BTC_JPY')
    while thread.is_connected != True: 
        time.sleep(1)
        print('connecting...')
    while True:
        print(bfrt.get())
#        time.sleep(0.5)
else:
    print('lita')