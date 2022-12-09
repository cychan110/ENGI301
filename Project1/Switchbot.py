# Importing libraries
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time
import board
import busio
import adafruit_sht31d

# Initializing pins and variables
servo1 = "P1_33" #for turning switch on
servo2 = "P1_36" #for turning switch off
BTinput = 0
BT = "P1_3" #pin connected to USB breakout board, which has Bluetooth module plugged in

# Setting servos to neutral position
PWM.start(servo1,7.5,50)
time.sleep (1)
PWM.stop(servo1)
PWM.cleanup()
PWM.start(servo2,7.5,50)
time.sleep (1)
PWM.stop(servo2)
PWM.cleanup()

# Get bluetooth output
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
        
        # Getting temperature and humidity readout
        i2c = busio.I2C(board.SCL, board.SDA)
        sensor = adafruit_sht31d.SHT31D(i2c)
        print('Humidity: {0}%'.format(sensor.relative_humidity))
        print('Temperature: {0}C'.format(sensor.temperature))
        
    elif BTinput = 0 #Bluetooth signaling "Off" command     
        PWM.start(servo2,5,50) #rotating servo2 all the way right
        time.sleep (1.0)
        PWM.start(servo2,7.5,50) #resetting servo2 to neutral
        time.sleep (1.0)
        PWM.stop(servo2)
        PWM.cleanup()
        
        # Getting temperature readout
        i2c = busio.I2C(board.SCL, board.SDA)
        sensor = adafruit_sht31d.SHT31D(i2c)
        print('Humidity: {0}%'.format(sensor.relative_humidity))
        print('Temperature: {0}C'.format(sensor.temperature))
            
    else #standby state
        PWM.start(servo1,7.5,50)
        time.sleep (1)
        PWM.stop(servo1)
        PWM.cleanup()
        PWM.start(servo2,7.5,50)
        time.sleep (1)
        PWM.stop(servo2)
        PWM.cleanup()
