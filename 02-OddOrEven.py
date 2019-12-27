# Odd Or Even
# by RestlessPuppet
#11-9-19

num = input("Please enter a number: ")
num=int(num)
if num % 2 == 0:
	print("Your number is even!")
	if num % 4 == 0:
		print("(Your number also happens to be divisible by 4)")
else:
    print("Your number happens to be odd this time...")
input("(press enter to continue)")
