import BTCDataGetter.py
import DBWriter.py
import asyncio

class MasterThread:

    @classmethod
    def start(self):
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


MasterThread.start()