# Importing Libraries
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time
import Adafruit_BBIO.ADC as ADC


# Initializing pins and variables
servo1 = "P1_33" #for turning switch on
servo2 = "P1_36" #for turning switch off

BTinput = 0
BT = "P1_3" #pin connected to USB breakout board, which has Bluetooth module plugged in

temp = "P1_2" #temperature sensor

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
        
        # Getting temperature readout
        ADC.setup()
        while True:
            reading = ADC.read(temp)
            millivolts = reading * 1800  # 1.8V reference = 1800 mV
            temp_c = (millivolts - 500) / 10
            temp_f = (temp_c * 9/5) + 32
            print('C=%d F=%d' % (temp_c, temp_f))
            time.sleep(1)
        
    elif BTinput = 0 #Bluetooth signaling "Off" command     
        PWM.start(servo2,5,50) #rotating servo2 all the way right
        time.sleep (1.0)
        PWM.start(servo2,7.5,50) #resetting servo2 to neutral
        time.sleep (1.0)
        PWM.stop(servo2)
        PWM.cleanup()
        # Getting temperature readout
        ADC.setup()
        while True:
            reading = ADC.read(temp)
            millivolts = reading * 1800  # 1.8V reference = 1800 mV
            temp_c = (millivolts - 500) / 10
            temp_f = (temp_c * 9/5) + 32
            print('C=%d F=%d' % (temp_c, temp_f))
            time.sleep(1)
            
    else #standby state
        PWM.start(servo1,7.5,50)
        time.sleep (1)
        PWM.stop(servo1)
        PWM.cleanup()
        PWM.start(servo2,7.5,50)
        time.sleep (1)
        PWM.stop(servo2)
        PWM.cleanup()
        
    # Press CTRL + C to end program
