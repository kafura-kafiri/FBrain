import mraa
import time

# Initialize UART
u=mraa.Uart(0)

# Set UART parameters
u.setBaudRate(9600)
u.setMode(8, mraa.UART_PARITY_NONE, 1)
u.setFlowcontrol(False, False)

# Start a neverending loop waiting for data to arrive.
line = ''
flag = 0
while True:
    time.sleep(1)
    print(1)
    if u.dataAvailable():
        data_byte = u.readStr(1)
        if data_byte == '\n':
            if flag:
                print(line)
                line = ''
                flag = 1 - flag
            else:
                line += data_byte

