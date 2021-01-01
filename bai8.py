# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 15:49:06 2020

@author: Laptop Masstel
"""

import smtplib
import getpass
n = int(input('Số lần muốn gửi mail: '))
if n <= 0:
    print('Vui lòng nhập lại số lần muốn gửi mail')
else:
    email = input('Email của bạn là:')
    password = getpass.getpass('Password:')
    address = input('Người nhận: ')
    msg = input('Nội dung: ')
    
    client = smtplib.SMTP('smtp.gmail.com',587)
    client.starttls()
    client.login(email , password)
    for i in range(n):
        client.sendmail(email , address , msg)
    print(n,' tin nhắn đã được gửi tới ', address)
    client.quit()
    
