# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:53:33 2020

@author: Laptop Masstel
"""

x=[]
n=int(input("n= "))
i=0 
import random
for i in range(n):
        x.append(random.random())
print(x)
max=x[0]
i=1
while i<n:
    if max<x[i]:
        max=x[i]
    i=i+1
print("gia tri lon nhat la:",max)
print("ket thuc chuong trinh")