import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #clk
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #dt

# Set up event detection for both channels
GPIO.add_event_detect(18, GPIO.BOTH, bouncetime=2)
GPIO.add_event_detect(23, GPIO.BOTH, bouncetime=2)

count = 0

def rotary_callback(channel):
    current_time = time.time()
    global prev_time
    global prev_state
    global resistance
    global count
    global count2
    state = GPIO.input(channel)
    if channel == 18:
        if state != prev_state[0]:
            if state == 0 and count2 == 0:
                direction = "Clockwise 1"
                speed = current_time - prev_time
                if speed < 0.01:
                    resistance += 100
                else:
                    resistance += 1
                count = 1
                print(f"Direction: {direction}, Speed: {speed}, Resistance: {resistance}")
            elif count == 0 and count2 == 0:
                direction = "clockwise 2"
                speed = current_time - prev_time
                if speed < 0.01:
                    resistance += 100
                else:
                    resistance += 1
                count2 = 0
                print(f"Direction: {direction}, Speed: {speed}, Resistance: {resistance}")    
            else :
                count = 0
                count2 = 0
            prev_time = current_time
            prev_state[0] = state
            time.sleep(.05)
    else:
        if state != prev_state[1]:
            if state == 0 and count2 == 0:
                direction = "Counter clockwise 3"
                speed = current_time - prev_time
                if speed < 0.01:
                    resistance -= 100
                else:
                    resistance -= 1
                count = 1
                print(f"Direction: {direction}, Speed: {speed}, Resistance: {resistance}")
            elif count == 0:
                direction = "Counterclockwise 4"
                speed = current_time - prev_time
                if speed < 0.01:
                    resistance -= 100
                else:
                    resistance -= 1
                    count2 = 1
                print(f"Direction: {direction}, Speed: {speed}, Resistance: {resistance}")
            else :
                count = 0
                count2 = 0
            prev_time = current_time
            prev_state[1] = state
            time.sleep(.05)

prev_state = [1, 1]
prev_time = time.time()

# Add the callback function for both channels
GPIO.add_event_callback(18, rotary_callback)
GPIO.add_event_callback(23, rotary_callback)

resistance = 0
count = 0
count2 = 0
# Keep the program running
while True:
    time.sleep
