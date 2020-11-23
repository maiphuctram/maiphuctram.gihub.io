# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:58:46 2020

@author: Laptop Masstel
"""
x=[]
n=int(input("n= "))
i=0 
import random
for i in range(n):
        x.append(random.random())
print(x)
min=x[0]
i=1
while i<n:
    if min>x[i]:
        min=x[i]
    i=i+1
print("gia tri be nhat la:",min)
print("ket thuc chuong trinh")