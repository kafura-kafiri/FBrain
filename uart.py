import mraa
import time
import datetime
from config import db

iran_delta = datetime.timedelta(hours=3, minutes=30)

# Initialize UART
u = mraa.Uart(0)

# Set UART parameters
u.setBaudRate(9600)
u.setMode(8, mraa.UART_PARITY_NONE, 1)
u.setFlowcontrol(False, False)


def parse(line):
    params = line.split(',')[:3]
    params = [int(p.strip()) for p in params]
    params = {
        'date': datetime.datetime.now() + iran_delta,
        'quality': params[0],
        'attention': params[1],
        'meditation': params[2],
    }
    return params


def handle(line):
    data = parse(line)
    if data['quality'] != 200:
        db.insert(data)
        print('<< OK')


def start_provide():
    import _thread

    def someFunc():
        # Start a neverending loop waiting for data to arrive.
        line = ''
        flag = 0
        while True:
            time.sleep(1)
            while u.dataAvailable():
                data_byte = u.readStr(1)
                if data_byte == '\n':
                    if flag:
                        handle(line)
                    line = ''
                    flag = 1 - flag
                else:
                    line += data_byte

    _thread.start_new_thread(someFunc, ())
    pass