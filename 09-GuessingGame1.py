###################
# Guessing Game I
# by RestlessPuppet
# 11-10-19
####################

import random

a = random.randint(1, 100)
n = 0
g =0
b = 100

while g != a:
    while g != a:
        g = input("Try and guess a number between 1 and 100: ")
        if g == "quit":
            break
        else:
            g=int(g)
        n+=1
        if g < a:
            print("your guess was too low, try again! ")
        elif g > a:
            print("Your guess was too high, try again! ")        
        elif g ==a:
            print("CONGRATULATIONS! You guessed correctly, and it only took " +str(n)+" turns!")

    # n = int(n)    
    # if n < b:
        # b = n 
        # print("Your score of " + str(n) + " is a new high score this session")
    # elif n == b:
        # print("You have tied your session record")
    # else:
        # print("Your session record is " + str(b) + ". Better luck next time!")
    # a = input("Do you wiah to play again? (y/n) ")
    # if a ==y:
        # g = 0
        # a = random.randint(1, 100)
                  

