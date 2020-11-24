# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 15:49:06 2020

@author: Laptop Masstel
"""

import smtplib
	from email.mime.base import MIMEBase
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
    fromaddr = "maithiphuctram@gmail.com"
    toaddr = "maithiphuctram@gmail.com"
    msg = MIMEMultipart()    
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "bài 8"
    body = "thầy hơi ác ạ"
    
