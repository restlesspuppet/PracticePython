#############################
# Check Primality Functions 2.0
# By RestlessPuppet
# 11/23/19
#############################

def get_num(txt):
    return input(txt)

def isitPrime (number):
    prime = "Your number ("+ number + ") is prime!"
    not_prime = "Your number, " + number + " is not prime."
    print("\n")
    i = 2
    l = []
    while i < int(number):
        if int(number) % i ==0:
            l.append(i)
        i+=1
    if l != []:
        print(not_prime)
    elif l == []:
        print(prime)
    return;

num = get_num("Please enter a number: ")
while num != "":
    isitPrime(num)
    num = get_num("\n Enter a new number to try again or ENTER to exit: ")
    
