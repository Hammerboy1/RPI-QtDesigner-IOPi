#importing libraries
import smbus

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

IO_write = None
IO_read = None
IO_output = None

#function to acces outputpins
def write_pin(IO_write):

        adress_array = [0x20, 0x21, 0x22, 0x23, 0x24, 0x25]

        port_array = [0x14, 0x15]

        #pin_array = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
        pin_array = [0xfe, 0xfd, 0xfb, 0xf7, 0xef, 0xdf, 0xbf, 0x7f]


        adress = adress_array[int((IO_write-1)/16)]

        port = port_array[int(((IO_write-1)/8)%2)]

        pin = pin_array[7 & (IO_write - 1)]

        return(adress,port,pin)

#function to acces inputpins
def read_pin(IO_read):

        adress_array = [0x20, 0x21, 0x22, 0x23, 0x24, 0x25]

        port_array = [0x12, 0x13]

        pin_array = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]



        adress = adress_array[int((IO_read-1)/16)]

        port = port_array[int(((IO_read-1)/8)%2)]

        pin = pin_array[7 & (IO_read - 1)]

        return(adress,port,pin)

#function to set outputpins
def set_output(IO_output):

        #setting pins as inputs
        #bus.write_byte_data(adress_20,IO_DIR_A,0x00)
        #bus.write_byte_data(adress_20,IO_DIR_B,0x00)
        #bus.write_byte_data(adress_21,IO_DIR_A,0x00)
        #bus.write_byte_data(adress_21,IO_DIR_B,0x00)
        #bus.write_byte_data(adress_22,IO_DIR_A,0x00)
        #bus.write_byte_data(adress_22,IO_DIR_B,0x00)
        #bus.write_byte_data(adress_23,IO_DIR_A,0x00)
        #bus.write_byte_data(adress_23,IO_DIR_B,0x00)
        #setting pins as pull-up inputs
        #bus.write_byte_data(adress_24,IO_DIR_A,0xff)
        #bus.write_byte_data(adress_24,IO_DIR_B,0xff)
        #bus.write_byte_data(adress_25,IO_DIR_A,0xff)
        #bus.write_byte_data(adress_25,IO_DIR_B,0xff)
        #bus.write_byte_data(adress_24,0x0d,0x00)
        #bus.write_byte_data(adress_24,0x0c,0x00)
        #bus.write_byte_data(adress_25,0x0d,0x00)
        #bus.write_byte_data(adress_25,0x0c,0x00)
        
        adress_array = [0x20, 0x21, 0x22, 0x23, 0x24, 0x25]

        direction_array = [0x00, 0x01]

        #pin_array = [0xfe, 0xfd, 0xfb, 0xf7, 0xef, 0xdf, 0xbf, 0x7f]


        adress = adress_array[int((IO_output-1)/16)]

        direction = direction_array[int(((IO_output-1)/8)%2)]

        pin = pin_array[7 & (IO_output - 1)]

        bus.write_byte_data(adress,direction,pin)

        return(adress,direction,pin)

