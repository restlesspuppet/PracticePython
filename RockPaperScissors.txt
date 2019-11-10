#########################
# Rock Paper Scissors
# by RestlessPuppet
# 11-10-19
#########################

import random

pa = "y"

while pa == "y":
    c = random.randint(1, 3)
    if c == 1:
        comp = "rock"
    elif c == 2:
        comp = "scissors"
    elif c == 3:
        comp = "paper"
    
    user = input("Please enter a selection (rock, paper, or scissors): ")
    print("Your opponent selected " + comp)

    draw = "It's a draw"
    win = "You have won!"
    lose = "Your opponent has bested you this time"


    if user == "rock":
        if c ==1:
            print(draw)
        elif c == 2:
            print(win)
        elif c == 3:
            print(lose)
        
    elif user == "paper":
        if c ==1:
            print(win)
        elif c == 2:
            print(lose)
        elif c == 3:
            print(draw)
        
    elif user == "scissors":
        if c ==1:
            print(lose)
        elif c == 2:
            print(draw)
        elif c == 3:
            print(win)
    pa = input("Do you wish to play again? (y/n): ")


    

