# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:12:47 2020

@author: Laptop Masstel
"""
# while
n=int(input("n: "))
i=1
while i <= n:
    print('Đây là chương trình giải phường trình bậc nhất có dạng: ax + b = 0')
    a = int(input('a = '))
    b = int(input('b = '))       
    if a == 0:
        if b !=0:
            print("pt vô nghiệm")
        else:
            print("pt có vô số nghiệm")        
    else:
        if b != 0:
            print("pt có nghiệm: ",-b/a)
        else:
            print("pt có nghiệm bằng 0")
    i+=1
print("the end")




#For
for i in range(0,n):
     print('Đây là chương trình giải phường trình bậc nhất có dạng: ax + b = 0') 
     a= int(input("a="))
     b= int(input("b="))      
     if a == 0:
        if b !=0:
            print("pt vô nghiệm")
        else:
            print("pt có vô số nghiệm")        
     else:
        if b != 0:
            print("pt có nghiệm: ",-b/a)
        else:
            print("pt có nghiệm bằng 0")
    
print("the end")
    