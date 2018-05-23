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
bus.write_byte_data(adress_20,IO_DIR_A,0x00)
bus.write_byte_data(adress_20,IO_DIR_B,0x00)
bus.write_byte_data(adress_21,IO_DIR_A,0x00)
bus.write_byte_data(adress_21,IO_DIR_B,0x00)
bus.write_byte_data(adress_22,IO_DIR_A,0x00)
bus.write_byte_data(adress_22,IO_DIR_B,0x00)
bus.write_byte_data(adress_23,IO_DIR_A,0x00)
bus.write_byte_data(adress_23,IO_DIR_B,0x00)
#setting pins as pull-up inputs
bus.write_byte_data(adress_24,IO_DIR_A,0xff)
bus.write_byte_data(adress_24,IO_DIR_B,0xff)
bus.write_byte_data(adress_25,IO_DIR_A,0xff)
bus.write_byte_data(adress_25,IO_DIR_B,0xff)
bus.write_byte_data(adress_24,0x0d,0x00)
bus.write_byte_data(adress_24,0x0c,0x00)
bus.write_byte_data(adress_25,0x0d,0x00)
bus.write_byte_data(adress_25,0x0c,0x00)

Roof_write = [83,81,86,84,82]
Roof_read = [51,50,54,53,55]
Roof_in = [4,2,32,16,64]
Roof_result = [0,0,0,0,0]

#check if cable is OK
def check():
        for out in range(0,5):
                adress_in,port_in,pin_in = IO.read_pin(Roof_read[out])
                adress_out,port_out,pin_out = IO.write_pin(Roof_write[out])

                bus.write_byte_data(adress_out,port_out,0)
                bus.write_byte_data(adress_in,port_in,0)
                time.sleep(0.1)
                bus.write_byte_data(adress_out,port_out,pin_out)
                time.sleep(0.1)
                read = bus.read_byte_data(adress_in,port_in)
                time.sleep(0.1)
                bus.write_byte_data(adress_out,port_out,0)

                if read == Roof_in[out]:
                        Roof_result[out] = 1
                if read != Roof_in[out]:
                        Roof_result[out] = 0
                print ("Roof_write-->", Roof_write[out], "Roof_read-->", Roof_read[out], "read-->", read, "result-->", Roof_result[out])
                                
                out = out +1

        return(Roof_result)
def check()
