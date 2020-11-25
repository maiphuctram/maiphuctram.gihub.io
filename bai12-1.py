# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:46:22 2020

@author: Laptop Masstel
"""

import random
list1=[]
a= random.randint(50,1000)
print(a)
for i in range(a):
  list1.append(random.randint(-1000,1000))
print(list1)
list2=[]
for i in range(a):
  list2.append(random.uniform(-1000.0,1000.0))
print(list2)