import os
import time
import RPi.GPIO as GPIO

#Change this to whatever temperature you want the fan to kick on at.
maxTemp = 45 #Celsius
#Sets the time to wait in between checks
waitTime = 5 #seconds

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.OUT)
while(True):
    temperature = os.popen('vcgencmd measure_temp').readline()
    tempInC = float(temperature.replace("temp=","").replace("'C\n",""))
    if(tempInC >= maxTemp):
        GPIO.output(8, True)
    else:
        GPIO.output(8, False)
    time.sleep(waitTime)
