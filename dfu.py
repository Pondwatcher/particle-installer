#!/usr/bin/env python

import serial
import sys
yellCycles=10000000
baudRate = 14400
neutralBaudRate = 9600
portName = "/dev/ttyACM0"

if len(sys.argv) > 1:
  portName = sys.argv[1]

for i in range(yellCycles):
    try:
        ser = serial.Serial(portName, baudRate)
        ser.close()
        sys.exit()
    except Exception as e:
        print e
        pass
    try:
        ser = serial.Serial(portName, neutralBaudRate)
        ser.close()
        sys.exit();
    except Exception as e:
        print e
        pass


