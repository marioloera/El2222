#definitions
#import RPi.GPIO as GPIO #add GPIO library
import pigpio
import time #add time library


pi=pigpio.pi()
class Led:
	ledCount=0
	def __init__(self, pinNum):
		self.pinNum=pinNum
		self.PWM_Value=0
		pi.set_mode(self.pinNum,pigpio.OUTPUT)
		Led.ledCount += 1
		print "Creat Led at pin number:",self.pinNum
		#print "Total Led Created, number of leds: %d" %Led.ledCount 
		#print ("Led Created, number of leds: " +str(Led.ledCount)) 
	def setPWM(self,PWM_Value):
		if PWM_Value>255:
			PWM_Value=255
		self.PWM_Value=PWM_Value
		pi.set_PWM_dutycycle(self.pinNum,self.PWM_Value)
		print "Set PWM value to:", self.PWM_Value, "of pin number:",self.pinNum 
	def displayLed(self):
		print "pin number:",self.pinNum, ". PWM value:", self.PWM_Value

	def __del__(self):
		pi.set_PWM_dutycycle(self.pinNum,0)
		print "destroyed"

#create pbjects LED(pinNumer)
ledCenter=Led(26)
ledLeft=Led(19)
ledRight=Led(13)

#program
PWM_Value=0
ledCenter.setPWM(150)
try:
	while True:
		ledLeft.setPWM(PWM_Value)
		ledRight.setPWM(2*PWM_Value)
		time.sleep(0.5)#sleep time in seconds
		PWM_Value+=20
		if PWM_Value>255:
			PWM_Value=0
			print("reset\n")
except KeyboardInterrupt:
	del ledLeft
	del ledCenter
	del ledRight
	pi.stop()
