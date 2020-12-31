import random
from random import randint

def key_gen():
    keylist = random.choice('abcdefghijklmnopqrstuvwxyz')
    return keylist

lis=[]

n = random.randint(49,101)
for i in range(n):
    n = random.randint(1,6)
    list_name = ''
    for i in range(n):
        list_name = list_name + key_gen()
    age = randint(1, 100)
    dic = {'name': list_name, "age": age}
    lis.append(dic)
print(lis)
