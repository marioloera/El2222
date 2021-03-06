#definitions
import RPi.GPIO as GPIO #add GPIO library
import time #add time library
import random
GPIO.setmode(GPIO.BOARD) #set how to refer the RPi pins
#hardware output
led=37 #pin number for the led
ledRight=33 #pin number for the led
ledLeft=35 #pin number for the led
#hardware inputs
ButtonRight=38
ButtonLeft=40
#outputs
GPIO.setup(led,GPIO.OUT)#defined pin as output
GPIO.setup(ledRight,GPIO.OUT)#defined pin as output
GPIO.setup(ledLeft,GPIO.OUT)#defined pin as output
#inputs
GPIO.setup(ButtonRight,GPIO.IN)#defined pin as input
GPIO.setup(ButtonLeft,GPIO.IN)#defined pin as input
#Internal variables
CountPushLeft=0
CountPushRight=0
Left=0
Right=0
#program
print("Hola")
name=input('What is the name of p1? ') 
info=[str]*2
info[0]=name
name=input('What is the name of p2? ') 
info[1]=name
print("in the left  p1: "+info[0])
print("in the right p2: "+info[1])
print("*****PLAY*****")
try:
	while True:
		GPIO.output(led,1) #turn on the led
		time.sleep(random.uniform(3,6))
		GPIO.output(led,0) #turn off led
		while GPIO.input(ButtonLeft) and GPIO.input(ButtonRight):
			pass
		
		#check hardware and store the state
		if GPIO.input(ButtonLeft)==False:
			Left=1
		if GPIO.input(ButtonRight)==False:
			Right=1

		#if the bottons were pressed
		if Left:
			Left=0
			CountPushLeft+=1
			print("Left button pressed: "+str(CountPushLeft))
			while GPIO.input(ButtonLeft)==False:
				GPIO.output(ledLeft,1) #turn on the led
			GPIO.output(ledLeft,0) #turn off led
		if Right:
			Right=0
			CountPushRight+=1
			print("Right button pressed: "+str(CountPushRight))
			while GPIO.input(ButtonRight)==False:
				GPIO.output(ledRight,1) #turn on the led
			GPIO.output(ledRight,0) #turn off led
except KeyboardInterrupt:
	if CountPushLeft>>CountPushRight:
		print("\nP1: "+info[0]+"  won") 
	if CountPushRight>>CountPushLeft:
		print("\nP2: "+info[1]+"  won") 
	if CountPushRight==CountPushLeft:
		print("\nDraft")
	print("Score:\n"+info[0]+": "+str(CountPushLeft)+"\n"+info[1]+": "+str(CountPushRight))
	GPIO.cleanup() #clean up












































































