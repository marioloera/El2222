#definitions
import RPi.GPIO as GPIO #add GPIO library
import time #add time library
import random
GPIO.setmode(GPIO.BOARD) #set how to refer the RPi pins
led=37 #pin number for the led
ledRight=33 #pin number for the led
ledLeft=35 #pin number for the led
ButtonRight=38
ButtonLeft=40
#outputs
GPIO.setup(led,GPIO.OUT)#defined pin as output
GPIO.setup(ledRight,GPIO.OUT)#defined pin as output
GPIO.setup(ledLeft,GPIO.OUT)#defined pin as output
#inputs
GPIO.setup(ButtonRight,GPIO.IN)#defined pin as input
GPIO.setup(ButtonLeft,GPIO.IN)#defined pin as input
#program
try:
	while True:
		GPIO.output(led,1) #turn on the led
		#time.sleep(random.uniform(3,6))
		time.sleep(3)
		GPIO.output(led,0) #turn off led
		while GPIO.input(ButtonLeft) and GPIO.input(ButtonRight):
			pass
		if GPIO.input(ButtonLeft)==False:
			print("Left button pressed")
			GPIO.output(ledLeft,1) #turn on the led
		if GPIO.input(ButtonRight)==False:
			print("Right button pressed")
			GPIO.output(ledRight,1) #turn on the led
		time.sleep(2)
		GPIO.output(ledRight,0) #turn off led
		GPIO.output(ledLeft,0) #turn off led
except KeyboardInterrupt:
	GPIO.cleanup() #clean up












































































