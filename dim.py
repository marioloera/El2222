#definitions
#import RPi.GPIO as GPIO #add GPIO library
import pigpio
import time #add time library
pi=pigpio.pi()
led=26#pin number for the led
pi.set_mode(led,pigpio.OUTPUT)
PWM_Value=0
#program
try:
	while True:
		time.sleep(0.5)#sleep time in seconds
		pi.set_PWM_dutycycle(led,PWM_Value)
		PWM_Value+=20
		print("PWM_Value="+str(PWM_Value))
		if PWM_Value>255:
			PWM_Value=0
			print("reset\n")
except KeyboardInterrupt:
	pi.set_PWM_dutycycle(led,0)
	pi.stop()
