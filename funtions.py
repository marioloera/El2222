# -*- coding: utf-8 -*-
import random
import time

class Game:
        def __init__(self):
            self.state=1
            self.set=1
            self.n=3
            self.n_size=16
            self.vel=2
            self.max_vel=5
            self.answer=1
            self.score=0
            self.led_min=1
            self.led_max=4
            self.array=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            self.guess=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        def play(self):
            print "game"
            self.score=0
            self.leds_sequence()
            self.guessing()
            self.evaluation()

        def leds_sequence(self):
            for i in range(0,game.n):
                game.array[i]=random.randrange(game.led_min,game.led_max+1)
                print (str(i) + ": " + "L" + str(game.array[i]) )
                #led turn on
                #GPIO.output(game.array[i],1)#turn on led
                time.sleep(1/game.vel)#sleep time in seconds
                #GPIO.output(game.array[i],0)#turn on led
                #turn led off
            return;

        def guessing(self):
            print "press the secuence now: "
            for i in range(0,game.n): #to iterate on the factors of the number
                #push button
                num=input('What is the next led: ')
                game.guess[i]=num
                #led turn on
            return;

        def evaluation(self):
            #evaluation
            for i in range(0,game.n):
                if game.array[i]==game.guess[i]:
                    game.answer*=1
                    game.score+=1
                    sign="  = "
                    text="    correct!"
                else:
                    game.answer*=0
                    sign=" != "
                    text="  incorrect!"

                print (str(i) + ": " + "L" + str(game.array[i]) + sign + "B" + str(game.guess[i]) + text + " answer value " + str(game.answer))

            if game.answer==1:
                print "Contratulations you win"
                #green leed on
                #sleep
            else:
                print ("you score " + str(game.score) + " out of " + str(game.n))
            return;

        def set_size(self):
            print "settings 1 button to increase 2 to set"
            game.n=0
            game.set=1
            while game.set==1:
                game.set=input('incrase?')
                if game.set==1:
                    game.n+=1
                    print game.n
            return;


game=Game()

game.state=input('press 1 button to play press 2 buttons for game setting: ')
#one button increase
#two buttons configurations
while game.state!=3:
    if game.state==1:
        game.play()
    elif game.state==2:
        game.set_size()
        game.play()
    game.state=input('press 1 button to play again press buttons 2 for setting press 3 to finish: ')



