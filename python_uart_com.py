import serial
import time

uartDataSettings = serial.Serial('COM3')

uartDataSettings.baudrate = 115200  # set Baud rate
uartDataSettings.bytesize = 8   # Number of data bits = 8
uartDataSettings.parity = 'N'   # No parity
uartDataSettings.stopbits = 1   # Number of Stop bits = 1

time.sleep(1)   # in Seconds

uartDataSettings.write(b'A')  # Transfer byteArray (8 bit)

uartDataSettings.close()






