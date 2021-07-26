#****************************************************************************************
#* @author  Bhargav Malasani
#* @version V1.0
#* @date    19-Jul-2021
#* @brief   Raspberry Pi HC-05 bluetooth COM Echo: Python 3 with serial lib
#****************************************************************************************

import serial 
ser=serial.Serial("/dev/ttyS0", baudrate=9600,timeout=2.0)
while 1: 
     data=ser.readline()
     if data=='close\r\n' or data=='close' :
         print('closing......') 
         ser.write('closing......')   
         break
     if(data!='') :
         print ('Data: '+data)
         ser.write(data)
ser.close()
exit() 