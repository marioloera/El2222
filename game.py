#EL2222 - project
#Mario Loera Lozano
#Last change 2016-march-03

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
PIN_l1=40
PIN_l2=38
PIN_l3=36
PIN_l4=32
PIN_lgreen=8
PIN_lred=10

class Game:
        def __init__(self):
            self.state=1
            self.set=1
            self.size=3
            self.size_max=15
            self.vel=5.0
            self.max_vel=5.0
            self.answer=1
            self.score=0
            self.led_min=1
            self.led_max=4
            self.array=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            self.guess=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        def play(self):
            print "game"
            self.score=0
            lred.blink(5,30)
            self.leds_sequence()
            lred.off()
            lgreen.blink(5,50)
            self.guessing()
            lgreen.off()
            self.evaluation()

        def leds_sequence(self):
            time.sleep(.5)
            for i in range(0,self.size):
                self.array[i]=random.randrange(self.led_min,self.led_max+1)
                print ("L" + str(self.array[i]) + "  :" + str(i+1) )
                time.sleep(1.0/self.vel)
                #led turn on
                dic_Led[self.array[i]].on()
                #sleep time in seconds
                time.sleep(1.0/self.vel)
                #turn led off
                dic_Led[self.array[i]].off()
            return;

        def guessing(self):
            print "press the secuence now: "
            for i in range(0,self.size): #to iterate on the factors of the number
                #print "What is the next led: "
                self.guess[i]=self.get_button(1)
            return;

        def evaluation(self):
            #evaluation
            self.answer=1
            for i in range(0,self.size):
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
                print "Contratulations you won!"
                self.size+=1
                if self.size>self.size_max:
                    self.size=self.size_max
                lgreen.on()
                time.sleep(2.0)
                lgreen.off()

            else:
                print ("you score " + str(self.score) + " out of " + str(self.size))
                lred.on()
                time.sleep(2.0)
                lred.off()
            return;

        def set_size(self):
            print "set size: press B1 increase, B2 for set"
            self.size=1
            self.set=1
            while self.set==1:
                print ("size: " + str(self.size))
                self.show_binary_num()
                self.set=self.get_button(0)
                if self.set==1:
                    self.size+=1
                    if self.size>self.size_max:
                        self.size=1
            self.leds_off()
            return;

        def show_binary_num(self):
            k=self.size
            self.leds_off()
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
                print "increase velocity?"
                l1.blink(self.vel/2,50)
                self.set=self.get_button(0)
                if self.set==1:
                    self.vel+=1.00
                    if self.vel>self.max_vel:
                        self.vel=1.00
                    print ("vel: " + str(self.vel))
            l1.off()
            return;

        def get_button(self,light):
            result=0
            while result==0:
                if b1.pressed_once(light):
                    result=b1.num
                if b2.pressed_once(light):
                    result=b2.num
                if b3.pressed_once(light):
                    result=b3.num
                if b4.pressed_once(light):
                    result=b4.num
            return result;

        def leds_off(self):
            l1.off()
            l2.off()
            l3.off()
            l4.off()
            return;

class Led:
        def __init__(self, Num, PinNum):
                self.num=Num
                self.pinNum=PinNum
                GPIO.setup(self.pinNum,GPIO.OUT)#defined pin as output
                self.freq=200
                self.pwm = GPIO.PWM(self.pinNum,self.freq)
                self.pwm.start(0)
                print ("Led " + str(self.num) + " created at pin number:" + str(self.pinNum))

        def on(self):
            self.pwm.ChangeFrequency(self.freq)
            self.pwm.start(100)
            return;

        def blink(self,frequency,dc):
            self.pwm.ChangeFrequency(frequency)
            self.pwm.start(dc)
            return;

        def off(self):
            self.pwm.start(0)
            return;

        def __del__(self):
            self.pwm.stop()

class Button:
        def __init__(self, Num, PinNum):
                self.num=Num
                self.pinNum=PinNum
                self.previus_state=0
                GPIO.setup(self.pinNum,GPIO.IN)#defined pin as input
                print("B" + str(self.num) + " created at pin:  "+ str(self.pinNum))

        def pressed_once(self,light):
            value = False
            if GPIO.input(self.pinNum)==False:
                self.previus_state=0
                value = False
            if GPIO.input(self.pinNum) and self.previus_state==0:
                self.previus_state=1
                value = True
                if light==1:
                    dic_Led[self.num].on()
                while GPIO.input(self.pinNum):
                    pass #keep led state and program here
                if light==1:
                    dic_Led[self.num].off()
            return value;

        def is_pressed(self):
            return GPIO.input(self.pinNum);

GPIO.cleanup()

#create objects Button(pinNumber)
b1=Button(1,PIN_b1)
b2=Button(2,PIN_b2)
b3=Button(3,PIN_b3)
b4=Button(4,PIN_b4)

#create objects LED(pinNumber)
l1=Led(1,PIN_l1)
l2=Led(2,PIN_l2)
l3=Led(3,PIN_l3)
l4=Led(4,PIN_l4)
lgreen=Led(5,PIN_lgreen)
lred=Led(6,PIN_lred)

dic_Led = {1:l1, 2:l2, 3:l3, 4:l4, 5:lgreen, 6:lred};

#create game
game=Game()


while game.state!=4:
    print "Press: B1 to play, B2 for set_size, B3 for set_vel, B4 to exit:"
    l1.blink(15,10)
    l2.blink(15,10)
    l3.blink(15,10)
    l4.blink(15,10)

    game.state=game.get_button(1)
    game.leds_off()

    if game.state==1:
        game.play()
    elif game.state==2:
        lgreen.blink(10,50)
        lred.blink(10,30)
        game.set_size()
        lgreen.off()
        lred.off()
        game.play()
    elif game.state==3:
        game.set_vel()
        game.play()

#delete objects
del l1
del l2
del l3
del l4
del lred
del lgreen
GPIO.cleanup() #clean up
