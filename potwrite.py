import pigpio
import time
cs1 = 8
clk = 11
sdi = 10
sdo = 9

pi= pigpio.pi()
pot = pi.spi_open(0, 97600)
resistance = 100

def potProgram(pot, resistance):
    if (resistance > 9400)
        resistance = 9400
print(round(128*(resistance*100)/9400))


#def write_pot():
#    pi1.write(cs1,0)
#    pi1.write(clk,0)
#    cmd = 0b0000000010000001
   


#write_pot()






#pi = pigpio.pi()

#MCP4231_ADDR = 0x28

#MCP4231_WRITE_WIPER0 = 0x00
#MCP4231_WRITE_WIPER1 = 0x10
#resistance_value = 128

#pi.i2c_write_byte_data(MCP4231_ADDR, MCP4231_WRITE_WIPER0, resistance_value)
#pi.i2c_write_byte_data(MCP4231_ADDR, MCP4231_WRITE_WIPER1, resistance_value)


#print("test")




