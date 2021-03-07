# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 23:30:18 2021

@author: Laptop Masstel
"""


import pandas as pd
import random
df=pd.read_csv('C:/Users/Laptop Masstel/Downloads/danh-sach-sinh-vien - Trang tính1.csv', sep=',',header=None)


dfs = df.sample(7)
dfs.to_csv('C:/Users/Laptop Masstel/Downloads/Bảng tính chưa có tiêu đề - Trang tính1.csv')
print(dfs)



