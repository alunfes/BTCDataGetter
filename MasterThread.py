import BTCDataGetter
import DBWriter
import asyncio
import BTCData

class MasterThread:

    @classmethod
    async def start(cls):
        BTCData.BTCExecutionData.initialize()
        bfd = BTCDataGetter.BtcFxDataGetter('lightning_executions_','FX_BTC_JPY')
        dw = DBWriter.DBWriter()
        await dw.testHello()
        num_failed = 0

        while bfd.is_connected() != True or num_failed < 50: 
            print('connecting...', bfd.is_connected())
            num_failed +=1
            while bfd.is_connected():
                await dw.testCall()
        bfd.disconnect()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(MasterThread.start())