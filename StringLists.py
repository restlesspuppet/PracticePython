############################
# String Lists
# by RestlessPuppet
# 11-9-19
############################

str = input("please enter any random string: ")
rts = str[::-1]
if str == rts:
    print("Your string is a palindrome!")
else:
    print("Not a palindrome")
