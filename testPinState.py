#importing libraries
import smbus
import time
import IO

bus = smbus.SMBus(1)
# Device address
adress_20  = 0x20 
adress_21 = 0x21
adress_22 = 0x22
adress_23 = 0x23
adress_24 = 0x24
adress_25 = 0x25
# Pin direction register
IO_DIR_A = 0x00 
IO_DIR_B = 0x01
# Register for outputs
OLATA  = 0x14 
OLATB  = 0x15
# Register for inputs
GPIOA  = 0x12 
GPIOB  = 0x13

#setting pins as outputs
bus.write_byte_data(adress_24,IO_DIR_A,0x00)
bus.write_byte_data(adress_24,IO_DIR_B,0x00)
bus.write_byte_data(adress_25,IO_DIR_A,0x00)
bus.write_byte_data(adress_25,IO_DIR_B,0x00)
#setting pins as pull-up inputs
bus.write_byte_data(adress_20,IO_DIR_A,0xff)
bus.write_byte_data(adress_20,IO_DIR_B,0xff)
bus.write_byte_data(adress_21,IO_DIR_A,0xff)
bus.write_byte_data(adress_21,IO_DIR_B,0xff)
bus.write_byte_data(adress_22,IO_DIR_A,0xff)
bus.write_byte_data(adress_22,IO_DIR_B,0xff)
bus.write_byte_data(adress_23,IO_DIR_A,0xff)
bus.write_byte_data(adress_23,IO_DIR_B,0xff)
bus.write_byte_data(adress_20,0x0d,0x00)
bus.write_byte_data(adress_20,0x0c,0x00)
bus.write_byte_data(adress_21,0x0d,0x00)
bus.write_byte_data(adress_21,0x0c,0x00)
bus.write_byte_data(adress_22,0x0d,0x00)
bus.write_byte_data(adress_22,0x0c,0x00)
bus.write_byte_data(adress_23,0x0d,0x00)
bus.write_byte_data(adress_23,0x0c,0x00)

L1_write = [0,83,83,83,67,66,65,86]
L1_read = [0,1,2,3,4,5,6,7]
L1_in = [0,0,0,0,8,16,32,64]

#check if cable is OK
def check():
        for out in range(1,2):
                while True:                 
                        adress_in,port_in,pin_in = IO.read_pin(1)                               
                                                                                     
                        time.sleep(1)
                        read = bus.read_byte_data(adress_in,port_in)
                            
                        print ("L1_write-->", L1_write[out], "L1_read-->", L1_read[out], "read-->", read)                        
                
check()
