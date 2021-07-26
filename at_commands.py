#******************************************************************************
#* @author  Bhargav Malasani
#* @version V1.0
#* @date    19-Jul-2021
#* @brief   Raspberry Pi HC-05 bluetooth AT commands: Python 3 with serial lib
#******************************************************************************

import serial
ser=serial.Serial("/dev/ttyS0", baudrate=38400,timeout=5.0)
cmd='AT  \r\n'
ser.write(cmd.encode())
data=ser.readline()
data1=chr(int(data[:2],2))
print (data1)
ser.close()
exit()