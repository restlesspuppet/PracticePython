###################
# Guessing Game I
# by RestlessPuppet
# 11-10-19
####################

import random

a = random.randint(1, 10)
n = 0
g =0
while g != a:
    g = input("Try and guess a number between 1 and 10: ")
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
