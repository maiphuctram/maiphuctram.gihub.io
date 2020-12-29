# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 20:38:22 2020

@author: Laptop Masstel
"""

import random

def key_gen():
    keylist = random.choice('abcdefghijklmnopqrstuvwxyz')
    return keylist

number = 0
list_name = ''
while number < 5:
        number = number + 1
        list_name = list_name + key_gen()

print(list_name)

from random import randint

tuoi = randint(1, 80) 
print(tuoi)
dict = {'name': list_name, "age": tuoi}
print("tên: ",dict['name'],"-----","tuổi: ",dict['age'])