from readline import read_init_file
import numpy as np
import random

#list = ["g", "d"]
#print(list)
#newList = "{} {}".format(list[0], list[1])

#print(newList)
a = '123'
char = [c for c in a]
print(char)
print(list(char))
for i in range(9):
    colorinfo = []
    vector = np.base_repr(i, base=3)
    # mylist = [c for c in vector]
    print(int(vector[0]))

#for j in range(3):
#    bit = int(vector) >> j # use str[idx] instead
#    print(bit)
i = 1
g = 6
start = random.randint(0, 10)
while i < 20:
    g = i*10
    random.seed(3)
    print("start = ", start)
    i += 1
print("g = ", g)


