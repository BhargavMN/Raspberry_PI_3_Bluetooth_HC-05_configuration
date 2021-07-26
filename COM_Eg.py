#*****************************************************************************************************
#* @author  Bhargav Malasani
#* @version V1.0
#* @date    19-Jul-2021
#* @brief   Raspberry Pi HC-05 bluetooth COM mode Example: Python 3 with serial lib and RPi.GPIOlib
#*****************************************************************************************************


import serial
import io
import RPi.GPIO as GPIO


ser=serial.Serial("/dev/ttyS0", baudrate=9600,timeout=2.0)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
while 1:
      try:
         data=sio.readlines()
         print ("A")
         print data
      except KeyboardInterrupt:
         ser.close()
ser.close()
exit()