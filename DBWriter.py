import BTCData
import asyncio

class DBWriter:

    async def testCall(self):
        data = BTCData.BTCExecutionData.getFirstData()
        if data is not None:
            print('price={}, side={}, num={}'.format(data[2],data[1],BTCData.BTCExecutionData.getNumData()))

    async def testHello(self):
        print('hello this is DBWriter')

