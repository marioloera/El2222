#definitions
#add GPIO library
import RPi.GPIO as GPIO
#add time library
import time

#set how to refer the RPi pins
GPIO.setmode(GPIO.BOARD)

class Led:
        def __init__(self, pinNum):
                self.pinNum=pinNum
                GPIO.setup(pinNum,GPIO.OUT)#defined pin as output
                GPIO.output(self.pinNum,0)#turn off led
                print "Created Led at pin number:",self.pinNum

        def on(self):
            GPIO.output(self.pinNum,1)#turn on led

        def off(self):
            GPIO.output(self.pinNum,0)#turn off led

        def set(self, value):
            GPIO.output(self.pinNum, value)

        def __del__(self):
            GPIO.output(self.pinNum,0)#turn on led

class Button:
        def __init__(self, pinNum, name):
                self.pinNum=pinNum
                self.name=name
                self.previus_state=0
                GPIO.setup(self.pinNum,GPIO.IN)#defined pin as input
                print(self.name + " button created at pin:  "+ str(self.pinNum))

        def pressed_once(self):
            value = False
            if GPIO.input(self.pinNum)==False:
                self.previus_state=0
                value = False
            if GPIO.input(self.pinNum) and self.previus_state==0:
                print(self.name + " button pressed." )
                self.previus_state=1
                value = True
            return value;

        def is_pressed(self):
            return GPIO.input(self.pinNum);

a

#create objects Button(pinNumber)
b1=Button(37,"b1")
b2=Button(35,"b2")
b3=Button(33,"b3")
b4=Button(31,"b4")

#create objects LED(pinNumber)
l1=Led(13)
l2=Led(11)
l3=Led(7)
l4=Led(5)
lwin=Led(38)
lrun=Led(40)

#Internal variables
countPush=0

#program
try:
	while True:
                lrun.on()
                if GPIO.input(b4.pinNum)==False:
                        l4.off()
                        b4.previus_state=0
                if GPIO.input(b4.pinNum) and b4.previus_state==0:
			countPush+=1
                        print(b4.name + " button pressed: " + str(countPush) )
                        l4.on()
                        b4.previus_state=1




                l1.set(b1.pressed_once())
                l2.set(b2.is_pressed())
                l3.set(b3.is_pressed())


except KeyboardInterrupt:
        del l1
        del l2
        del l3
        del l4
        del lwin
        del lrun
	GPIO.cleanup() #clean up
	print("\nButton presed: "+str(countPush)+" times.")
























3


















































