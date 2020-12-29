# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:23:29 2020

@author: Laptop Masstel
"""

import numpy as np
a = np.array([(1, 2, 3),(4,5,6),(0,5,3)])
print(a) 
b= np.array([(0,4,6),(4,8,9),(0,1,7)])
print(b)
c=np.add(a,b)
print(c)
d=np.dot(a,b)
print(d)
n=np.transpose(a)
print(n)

import pandas as pd
n=pd.read_csv('C:/Users/Laptop Masstel/Downloads/Bảng tính chưa có tiêu đề - Trang tính1.csv')
print(n.head(10))




import matplotlib.pyplot as xyz
xyz.bar([0.24,1.20,2.24,3.20,4.22],[9,7,8,11,10],
label="dealine",width=.5)
xyz.bar([.65,1.65,2.55,3.85,4.85],[9,7,5,6,5],label="ngủ",width=.5)
xyz.legend()
xyz.xlabel('ngày')
xyz.ylabel('giờ')
xyz.title('biểu đồ')
xyz.show()
            


import matplotlib.pyplot as xyz
xyz.plot([5,10,15],[7,8,14])
xyz.title('biểu đồ')
xyz.show()



np.random.seed(1234)
df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['Col1', 'Col2', 'Col3', 'Col4'])
boxplot = df.boxplot(column=['Col1', 'Col2', 'Col3'])


