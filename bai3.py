# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 22:32:10 2020

@author: Laptop Masstel
"""
#cú pháp của câu lệnh lặp For như sau:
n = int(input("n: ")) #nhập sô nguyên n bất kì từ bàn phím
for i in range(0, n):     # điều kiện vòng lặp biến i chạy từ 0 đến n
      print("Hello Sky")  #in ra câu lệnh "Hello SKy"
print("the end")          #in ra câu lệnh "the end"
#muốn tăng bước nhảy cho for:
for i in range(0, n, 2):  #điều kiện vòng lặp biến i chạy từ 0 đến n với bước nhảy là 2
    print("Hello Sky")      #in ra câu lênh" Hello Sky"
print("the end")            #in ra câu lệnh "the end"
    
    