import datetime
import time
import threading

import _mraa

from config import csvs, current_user, iran_delta

# Initialize UART
u = _mraa.Uart(0)

# Set UART parameters
u.setBaudRate(9600)
u.setMode(8, _mraa.UART_PARITY_NONE, 1)
u.setFlowcontrol(False, False)


def parse(line):
    params = line.split(',')[:3]
    params = [int(p.strip()) for p in params]
    params = {
        'date': str(datetime.datetime.utcnow() + iran_delta),
        'quality': params[0],
        'attention': params[1],
        'meditation': params[2],
        'user_id': current_user['_id']
    }
    return params


def handle(line):
    data = parse(line)
    if data['quality'] != 200:
        csvs.insert(data)



class Threadish:
    def loop(self):
        line = ''
        flag = 0
        while True:
            time.sleep(1)
            while u.dataAvailable() and self.is_alive:
                data_byte = u.readStr(1)
                if data_byte == '\n':
                    if flag:
                        handle(line)
                    line = ''
                    flag = 1 - flag
                else:
                    line += data_byte

    def __init__(self):
        self.is_alive = False
        self.thread = threading.Thread(target=self.loop)
        self.thread.start()

thread = Threadish()