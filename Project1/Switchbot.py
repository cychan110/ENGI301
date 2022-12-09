# Importing Libraries
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time

# Initial Variables
servo1 = "P1_33" #for turning switch on
servo2 = "P1_36" #for turning switch off

BTinput = 0
BT = "P1_3" #pin connected to USB breakout board, which has Bluetooth module plugged in

# Returning Servos to Neutral Position
PWM.start(servo1,7.5,50)
time.sleep (1)
PWM.stop(servo1)
PWM.cleanup()
PWM.start(servo2,7.5,50)
time.sleep (1)
PWM.stop(servo2)
PWM.cleanup()

# Get Bluetooth Output
direction = GPIO.setup(BT, GPIO.IN)
bt = GPIO.input(BT) #BT output from USB/GPIO port

# Running the commands
while True:
    BTinput = GPIO.input(BT)    
    if BTinput = 0 #Bluetooth signaling "On" command     
        PWM.start(servo1,10,50) #rotating servo1 all the way left
        time.sleep (1.0)
        PWM.start(servo1,7.5,50) #resetting servo1 to neutral
        time.sleep (1.0)
        PWM.stop(servo1)
        PWM.cleanup()
        
    else BTinput = 0 #Bluetooth signaling "Off" command     
        PWM.start(servo2,5,50) #rotating servo2 all the way right
        time.sleep (1.0)
        PWM.start(servo2,7.5,50) #resetting servo2 to neutral
        time.sleep (1.0)
        PWM.stop(servo2)
        PWM.cleanup()
            
    
    # Press CTRL + C to end program
