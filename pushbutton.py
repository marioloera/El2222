#definitions
import RPi.GPIO as GPIO #add GPIO library
import time #add time library
GPIO.setmode(GPIO.BOARD) #set how to refer the RPi pins
led=37 #pin number for the led
ledRight=33 #pin number for the led
ledLeft=35 #pin number for the led
ButtonRight=38
countPush=0
previousState=1
#outputs
GPIO.setup(led,GPIO.OUT)#defined pin as output
GPIO.setup(ledRight,GPIO.OUT)#defined pin as output
#inputs
GPIO.setup(ButtonRight,GPIO.IN)#defined pin as input
#program
try:
	while True:
		GPIO.output(led,1) #turn on the led
		#time.sleep(random.uniform(3,6))
		#time.sleep(3)
		#GPIO.output(led,0) #turn off led
		if GPIO.input(ButtonRight):
			GPIO.output(ledRight,0)#turn off led
			previousState=1
		if GPIO.input(ButtonRight)==False and previousState==1:
			print("Right button pressed")
			GPIO.output(ledRight,1) #turn on the led
			countPush+=1
			previousState=0	
			#time.sleep(0.2)
except KeyboardInterrupt:
	GPIO.cleanup() #clean up
	print("\nButton presed: "+str(countPush))











































































