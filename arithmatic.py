#****************************************************************************************
#* @author  Bhargav Malasani
#* @version V1.0
#* @date    19-Jul-2021
#* @brief   Raspberry Pi HC-05 bluetooth arithmatic operations: Python 3 with serial lib
#****************************************************************************************

import serial
ser=serial.Serial("/dev/ttyS0", baudrate=9600,timeout=1000.0)
while 1:
    data=ser.readline()
        if data=='close\r\n' or data=='close' :
            print('closing......') 
            ser.write('closing......')   
            break
        if data!='' :    
            a=int(data)
            print('a: ', a)     
            data=ser.readline()
            if data!='' :
                operand=chr(int(data[0]))
                print('op: ', operand[0])
            
                data=ser.readline()
            
                if data!='' :
                    b=int(data)
                    print('b: ', b)
                
                    out = "ERROR"
        
                    if operand[0]=='+' :
                        out=a+b
                    if operand[0]=='-' :
                        out=a-b
                    if operand[0]=='*' :
                        out=a*b
                    if operand[0]=='/' :
                        out=a/b
                    out1=str(out)+'\r\n'
                    ser.write(out1.encode()      
ser.close()
exit()
