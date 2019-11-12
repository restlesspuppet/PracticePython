###############################
# List Overlap Comprehensions
# by RestlessPuppet
# 11-10-19
##############################

a = random.sample(range(1,10), random.randint(1,9))
b = random.sample(range(1,10), random.randint(1,9))

c = list(set([x for x in a for y in b if (x == y)]))

print(a,'\n',b,'\n',c)
