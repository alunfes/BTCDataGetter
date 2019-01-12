import BTCData.py
import asyncio

class DBWriter:

    async def testCall(self):
        data = BTCData.BTCExecutionData.getFirstData()
        if data is not None:
            print('price=' + data['price'] + ", side="+data['side'])

    async def testHello(self):
        print('hello')

