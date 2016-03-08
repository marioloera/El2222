#definitions
#add GPIO library
import RPi.GPIO as GPIO
#add time library
import time
import random

#set how to refer the RPi pins
GPIO.setmode(GPIO.BOARD)

#pin for push_buttons
PIN_b1=37
PIN_b2=35
PIN_b3=33
PIN_b4=31


#LEDs pinNumber
PIN_l1=13
PIN_l2=11
PIN_l3=7
PIN_l4=5
PIN_lgreen=38
PIN_lred=40

pin_leds = {1:PIN_l1, 2:PIN_l2, 3:PIN_l3, 4:PIN_l4};

class Game:
        def __init__(self):
            self.state=1
            self.set=1
            self.n=3
            self.n_max=15
            self.vel=1.0
            self.max_vel=5
            self.answer=1
            self.score=0
            self.led_min=1
            self.led_max=4
            self.array=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            self.guess=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        def play(self):
            print "game"
            self.score=0
            self.leds_sequence()
            self.guessing()
            self.evaluation()

        def leds_sequence(self):
            l1.off()
            l2.off()
            l3.off()
            l4.off()
            for i in range(0,self.n):
                self.array[i]=random.randrange(self.led_min,self.led_max+1)
                print (str(i) + ": " + "L" + str(self.array[i]) )
                time.sleep(1.0/self.vel)
                #led turn on
                GPIO.output(pin_leds[self.array[i]],1)#turn on led
                #sleep time in seconds
                time.sleep(1.0/self.vel)
                #turn led off
                GPIO.output(pin_leds[self.array[i]],0)#turn on led

            return;

        def guessing(self):
            print "press the secuence now: "
            for i in range(0,self.n): #to iterate on the factors of the number
                #push button
                num=input('What is the next led: ')
                self.guess[i]=num
                #led turn on
            return;

        def evaluation(self):
            #evaluation
            self.answer=1
            for i in range(0,self.n):
                if self.array[i]==self.guess[i]:
                    self.answer*=1
                    self.score+=1
                    sign="  = "
                    text="    correct!"
                else:
                    self.answer=0
                    sign=" != "
                    text="  incorrect!"

                print (str(i) + ": " + "L" + str(self.array[i]) + sign + "B" + str(self.guess[i]) + text + " answer value " + str(self.answer))

            if self.answer==1:
                print "Contratulations you win"
                GPIO.output(PIN_lgreen,1)
                time.sleep(2.0)
                GPIO.output(PIN_lgreen,0)
                #green leed on

            else:
                print ("you score " + str(self.score) + " out of " + str(self.n))
            return;

        def set_size(self):
            print "set size: press B1 increase, B2 for set"
            self.n=1
            self.set=1
            while self.set==1:
                print "current size"
                self.show_binary_num()
                self.set=input('incrase?')
                if self.set==1:
                    self.n+=1
                    if self.n>self.n_max:
                        self.n=1
                    print self.n
            return;

        def show_binary_num(self):
            k=self.n
            l1.off()
            l2.off()
            l3.off()
            l4.off()
            if k>7:
                l1.on()
                k-=8
                m="1 "
            else:
                m="0 "

            if k>3:
                l2.on()
                k-=4
                m+="1 "
            else:
                m+="0 "

            if k>1:
                l3.on()
                k-=2
                m+="1 "
            else:
                m+="0 "

            if k>0:
                l4.on()
                m+="1"
            else:
                m+="0"
            print m
            return;

        def set_vel(self):
            print "set vel: press B1 increase, B2 for set"
            self.vel=1.00
            self.set=1
            while self.set==1:
                self.set=input('incrase?')
                #blink led
                if self.set==1:
                    self.vel+=1
                    if self.vel>self.max_vel:
                        self.vel=1.00
                    print self.vel
            return;

        def get_button(self):
            result=0
            while result==0:
                if b1.is_pressed():
                    result=1
                if b2.is_pressed():
                    result=2
                if b3.is_pressed():
                    result=3
                if b4.is_pressed():
                    result=4
            return result;


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

#create objects Button(pinNumber)
b1=Button(PIN_b1,"b1")
b2=Button(PIN_b2,"b2")
b3=Button(PIN_b3,"b3")
b4=Button(PIN_b4,"b4")

#create objects LED(pinNumber)
l1=Led(pin_leds[1])
l2=Led(pin_leds[2])
l3=Led(pin_leds[3])
l4=Led(pin_leds[4])
lgreen=Led(PIN_lgreen)
lred=Led(PIN_lred)



#create game
game=Game()


print "Press: B1 to play, B2 for set_size, B3 for set_vel, B4 to exit:"
#game.state=input('Press: B1 to play, B2 for set_size, B3 for set_vel, B4 to exit: ')

game.state=game.get_button()
while game.state!=4:
    if game.state==1:
        game.play()
    elif game.state==2:
        game.set_size()
        game.play()
    elif game.state==3:
        game.set_vel()
        game.play()
    #game.state=input('Press: B1 to play, B2 for set_size, B3 for set_vel, B4 to exit: ')
    game.state=game.get_button()


#program
try:
	while True:
                lred.on()
                if GPIO.input(b4.pinNum)==False:
                        l4.off()
                        b4.previus_state=0
                if GPIO.input(b4.pinNum) and b4.previus_state==0:
                        print(b4.name + " button pressed." )
                        l4.on()
                        b4.previus_state=1

                l1.set(b1.pressed_once())
                l1.set(b1.is_pressed())
                l2.set(b2.is_pressed())
                l3.set(b3.is_pressed())


except KeyboardInterrupt:
        del l1
        del l2
        del l3
        del l4
        del lred
        del lgreen
	GPIO.cleanup() #clean up
























3


















































