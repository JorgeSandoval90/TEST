import pigpio
resistance = 0
pot_num = 0
pi1 = pigpio.pi()
h = pi1.spi_open(0,97600)
step = int(((128*resistance)/10000))

if(pot_num == 0):
    pi1.spi_write(h, [0b00000000,step])
else: 
    pi1.spi_write(h, [0b00010000,step])


