########################
# Fibonacci
# by RestlessPuppet
# 12/26/2019
########################

def fib(n):
    if n == 0:
        ls = [0]
    elif n == 1:
        ls = [0, 1]
    else:
        ls = [0, 1]
        for i in range(n-1):
            ls.append(ls[-2]+ls[-1])
    del ls[0]
    print(ls)


user_num = int(input("Please enter how many numbers you would like: "))
fib(user_num)
