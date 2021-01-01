# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 14:29:19 2020

@author: Laptop Masstel
"""


import os
file = input('Nhập tên file muốn tạo:')
type = input('Thể loại file:')
file = file + '.'+ type
f = open(file, mode = 'w')
f.write(input('Nhập nội dung:'))
f.close()
folder = input('Nhập đường dẫn của thư mục mà bạn muốn lưu lại:')
h = folder+'\\'+file
os.rename(file,h)
print('Đã lưu file.')