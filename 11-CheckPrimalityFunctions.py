#############################
# Check Primality Functions
# By RestlessPuppet
# 11/23/19
#############################


def get_num(txt):
    return input(txt)

num = get_num("Please enter a number: ")

while num != "":
    print("\n")
    i = 2
    l = []
    while i < int(num):
        if int(num) % i ==0:
            l.append(i)
        i+=1
    if l != []:
        print("Your number, " + num + " is not prime. It is divisible by "+str(l)+" as well as 1 and itself")
    elif l == []:
        print("Your number ("+ num + ") is prime!")

    num = get_num("\n Enter a new number to try again or ENTER to exit: ")
