# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 23:01:24 2020

@author: Laptop Masstel
"""

n=(3,6,8,1,4,7,-34,0)
i=0
for i in n:
  print(i)
  
#tính logarit
for i in n:
    if i > 0:
        import math
        print ("math.log(i) : ", math.log(i))
    else:
        print("không có giá trị log thỏa mãn")
print("the end")