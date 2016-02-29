# -*- coding: utf-8 -*-
import random
import time

class Game:
        def __init__(self):
            self.state=1
            self.set=1
            self.n=3
            self.n_max=15
            self.vel=2.0
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
            for i in range(0,self.n):
                self.array[i]=random.randrange(self.led_min,self.led_max+1)
                print (str(i) + ": " + "L" + str(self.array[i]) )
                #led turn on
                #GPIO.output(self.array[i],1)#turn on led
                time.sleep(2.0/self.vel)#sleep time in seconds
                #GPIO.output(self.array[i],0)#turn on led
                #turn led off
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
                #green leed on
                #sleep
            else:
                print ("you score " + str(self.score) + " out of " + str(self.n))
            return;

        def set_size(self):
            print "set size: press B1 increase, B2 for set"
            self.n=0
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
            #l1.off()
            #l2.off()
            #l2.off()
            #l3.off()
            if k>7:
                #l1.on()
                m="1 "
                k-=8
            else:
                m="0 "
            if k>3:
                #l2.on()
                k-=4
                m+="1 "
            else:
                m+="0 "
            if k>1:
                #l3.on()
                k-=2
                m+="1 "
            else:
                m+="0 "
            if k>0:
                #l1.on()
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






game=Game()

game.state=input('Press: B1 to play, B2 for set_size, B3 for set_vel, B4 to exit: ')

while game.state!=4:
    if game.state==1:
        game.play()
    elif game.state==2:
        game.set_size()
        game.play()
    elif game.state==3:
        game.set_vel()
        game.play()
    game.state=input('Press: B1 to play, B2 for set_size, B3 for set_vel, B4 to exit: ')



