import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #clk
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #dt
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #sw
previousValue = 1
resistance = 0
prev_time = time.time()

def rotary_changed():
    global previousValue
    global resistance
    global prev_time
    current_time = time.time()
    if previousValue != GPIO.input(18):
        if GPIO.input(18) == 0:
            if GPIO.input(23) == 0:
                direction = "anti-clockwise"
                speed = current_time - prev_time
                if speed < .2:
                    resistance -= 100
                else:
                    resistance -= 1
                print(f"Direction: {direction}, Resistance: {resistance}, Speed: {speed}")
                time.sleep(.1)
                prev_time = current_time
            else:
                direction = "clockwise"
                speed = current_time - prev_time
                if speed < .2:
                    resistance += 100
                else:
                    resistance += 1
                print(f"Direction: {direction}, Resistance: {resistance}, Speed: {speed}")
                time.sleep(.1)
                prev_time = current_time                
        previousValue = GPIO.input(18)
         
while True:
    if GPIO.input(24) == 0:
        count = 1
        print("Editing mode")
        time.sleep(.5)
        while count == 1:
            rotary_changed()
            if GPIO.input(24) == 0:
                print(f"Final resistance is : {resistance}")
                time.sleep(.5)
                count = 0
      
    
