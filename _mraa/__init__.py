import random
import datetime

class Uart:
    def __init__(self, pin):
        self.string = ''
        self.now = datetime.datetime.now()
        pass

    def setBaudRate(self, rate):
        pass

    def setMode(self, mode, uart_type, mute):
        pass

    def setFlowcontrol(self, b1, b2):
        pass

    def dataAvailable(self):
        if len(self.string) == 0:
            now = datetime.datetime.now()
            if now - self.now > datetime.timedelta(seconds=1):
                self.now = now
                quality = random.randint(0, 300)
                if quality > 200:
                    quality = 200
                attention = random.randint(0, 100)
                meditation = random.randint(0, 100)
                self.string = '{quality}, {attention}, {meditation}\n'.format(quality=quality, attention=attention,
                                                                            meditation=meditation)
        return len(self.string) != 0

    def readStr(self, length):
        result = self.string[:length]
        self.string = self.string[length:]
        return result

UART_PARITY_NONE = 0