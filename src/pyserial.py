#!/usr/bin/python

# Simple serial console utility passively dumps serial console messages

import serial
import time
import signal
import sys

class serial_console:
    def __init__(self, device, baud):
        self.device = device
        self.baud = baud
        self.ser = serial.Serial(device, baud)
        signal.signal(signal.SIGINT, self.signal_handler)
        print("open " + device + "Ok")

    def read(self):
        data = b''
        try:
            data = self.ser.readline()
        except serial.serialutil.SerialException:
            self.retry()

        return data

    def retry(self):
        self.ser.close()
        fail = True
        retry_count = 1
        while fail:
            time.sleep(1)
            try:
                self.ser = serial.Serial(self.device, self.baud)
                fail = False
                print("Ok Device " + self.device + " is online")
            except serial.serialutil.SerialException:
                fail = True
                print("retry " + str(retry_count) + " times")
                retry_count += 1

    def signal_handler(self, sig, frame):
        print("received keyboard interrupt, exit")
        sys.exit(0)

# RP2040 Serial test
sc = serial_console("/dev/ttyACM0", 115200)
print("creating console.. ")
while 1:
    data = sc.read()
    print("rp2040$ " + data.decode('ascii').rstrip())

