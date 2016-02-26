# -*- coding: utf-8 -*-
import random

min=0
max=1
print("Start")
led=random.randrange(min,max+1)
print("number: " + str(led))

n=5
array=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
guess=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
answer=1

#leds
for i in range(0,n):
    array[i]=random.randrange(min,max+1)
    #led turn on
    #delay

#game
for i in range(0,n): #to iterate on the factors of the number
    #push button
    guess[i]=random.randrange(min,max+1)
    #led turn on

#evaluation
for i in range(0,n):
    if array[i]==guess[i]:
        answer*=1
        sign="  = "
        text="    correct!"
    else:
        answer*=0
        sign=" != "
        text="  incorrect!"

    print (str(i) + ": " + "L" + str(array[i]) + sign + "B" + str(guess[i]) + text + " answer value " + str(answer))
