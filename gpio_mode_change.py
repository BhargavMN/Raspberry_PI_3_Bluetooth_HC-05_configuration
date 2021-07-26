#*******************************************************************************************************
#* @author  Bhargav Malasani
#* @version V1.0
#* @date    19-Jul-2021
#* @brief   Raspberry Pi HC-05 bluetooth AT and COM mode Changing: Python 3 with serial and RPi.GPIOlib
#*******************************************************************************************************

import time 
import sys 
import select 
import serial


try: 
    import RPi.GPIO as GPIO 
except RuntimeError: 
    print("Error importing RPi.GPIO")


#Pin Definations: 
pow_pin=37#pow: physical pin 37, bcm GPIO25
io_pin= 7 #Out: Physical pin 7, BCM GPIO7

#Pin setup 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(io_pin,GPIO.OUT)
GPIO.setup(pow_pin,GPIO.OUT)

GPIO.output(io_pin,GPIO.LOW)
GPIO.output(pow_pin,GPIO.LOW)
#Opening Serial Port 
ser=serial.Serial("/dev/ttyS0", baudrate=9600,timeout=5.0)
timeout =0.1

def bin_dec(bin_):
    bin1=bin_
    dec,i,n=0,0,0
    while(bin1!=0):
        dec1=bin1%10
        dec=dec+dec1*pow(2,i)
        bin1=bin1//10
        i=i+1
    return (dec)
        
        
    
def at(): 
    cmd='AT +NAME\r\n'
    ser.write(cmd.encode())
    data=ser.readline()
    print(data)
    


 
def com(): 
    while 1:
        data=ser.readline()
        if data=='close\r\n':
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
                    ser.write(out1.encode())
                    print('value='+out1)


while 1: 
    print ('Select Mode, AT: for AT mode, COM: for communication mode, close: to close application')
    i=input()
    if(i=='close'or i=='CLOSE'):
        GPIO.output(pow_pin,GPIO.LOW)
        exit()
    if(i=='AT'or i=='at'):
        GPIO.output(pow_pin,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(io_pin,GPIO.HIGH)
        GPIO.output(pow_pin,GPIO.HIGH)      
        print('AT mode enabled')
        ser.baudrate=38400
        at()
    elif(i=='COM'or i=='com'):
        GPIO.output(pow_pin,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(io_pin,GPIO.LOW)
        GPIO.output(pow_pin,GPIO.HIGH)  
        print('COM mode enabled')   
        ser.baudrate=9600
        ser.timeout=100
        com()
        
    else: 
        print ('Wrong Command')
ser.close()
exit()      
