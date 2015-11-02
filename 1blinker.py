#definitions
import RPi.GPIO as GPIO #add GPIO library
import time #add time library
GPIO.setmode(GPIO.BOARD) #set how to refer the RPi pins
led=37 #pin number for the led
GPIO.setup(led,GPIO.OUT)#defined pin as output
#program
GPIO.output(led,1) #turn on the led
time.sleep(1)#sleep time in seconds
GPIO.output(led,0) #turn off led
#clean up
GPIO.cleanup()












































































