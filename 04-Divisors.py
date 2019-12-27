##############
# Divisors
# by RestlessPuppet
# 11-9-19
###############

num = int(input("Enter a number: "))
i = 1
l = []
while i <= num:
    if num % i ==0:
        l.append(i)
    i+=1
print(str(l)+" are all divisible by " + str(num))

        
