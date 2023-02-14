import RPi.GPIO as GPIO
import time
import spidev

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up event detection for both channels
GPIO.add_event_detect(18, GPIO.BOTH, bouncetime=2)
GPIO.add_event_detect(23, GPIO.BOTH, bouncetime=2)

resistance = 0
prev_time = time.time()
#def rotary_callback(channel):
while True:
    current_time = time.time()
    global prev_state
    prev_state_clk = GPIO.input(18)
    if prev_state != GPIO.input(18):
        if GPIO.input(18) == 0:
            if GPIO.input(23) == 0:
                speed = current_time - prev_time
                print(speed)
                if speed < 0.02:
                    resistance -= 100
                else:
                    resistance -= 1
                direction = "anti clockwise"
                print(f"Direction: {direction}, Resistance: {resistance}" )
            else:
                speed = current_time - prev_time
                print(speed)
                if speed < 0.02:
                    resistance += 100
                else:
                    resistance += 1
                direction = "clockwise"
                print(f"Direction: {direction}, Resistance: {resistance}")
        prev_state = GPIO.input(18)
        prev_time = current_time
    #time.sleep



# Add the callback function for both channels
#GPIO.add_event_callback(18, rotary_callback)
#GPIO.add_event_callback(23, rotary_callback)


# Keep the program running
#while True:
#    time.sleep
