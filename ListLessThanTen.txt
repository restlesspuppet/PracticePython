# List Less Than Ten
# by RestlessPuppet
# 11/9/19
######################

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
num = int(input("Please enter a number: "))
for element in a:
  if element <= num:
    b.append(element)
print("the numbers on the list less than or equal to "+str(num)+" are: "+str(b))

