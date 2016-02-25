#definitions
import RPi.GPIO as GPIO #add GPIO library
import time #add time library
GPIO.setmode(GPIO.BOARD) #set how to refer the RPi pins
#HARDWARE CONFIGURATION
led=37 #pin number for the led
ledRight=33 #pin number for the led
ButtonRight=38
#outputs
GPIO.setup(led,GPIO.OUT)#defined pin as output
GPIO.setup(ledRight,GPIO.OUT)#defined pin as output
#inputs
GPIO.setup(ButtonRight,GPIO.IN)#defined pin as input
#Internal variables
countPush=0
previousState=0
#program
try:
	while True:
		GPIO.output(led,1) #turn on the led
		if GPIO.input(ButtonRight)==False:
			GPIO.output(ledRight,0)#turn off led
			previousState=0
		if GPIO.input(ButtonRight) and previousState==0:
			countPush+=1
			print("Right button pressed: "+str(countPush))
			GPIO.output(ledRight,1) #turn on the led
			previousState=1	
except KeyboardInterrupt:
	GPIO.cleanup() #clean up
	print("\nButton presed: "+str(countPush)+" times.")











































































