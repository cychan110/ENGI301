--------------------------------------------------------------------------
Switchbot
--------------------------------------------------------------------------
License:   
Copyright 2022 Jerry Chan
Based on library from
Copyright 2018 Babs Ogunbanwo
Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
-------------------------------------------------------------------------

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
            
    else # Standby state
        PWM.start(servo1,7.5,50)
        time.sleep (1)
        PWM.stop(servo1)
        PWM.cleanup()
        PWM.start(servo2,7.5,50)
        time.sleep (1)
        PWM.stop(servo2)
        PWM.cleanup()
