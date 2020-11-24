# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 23:51:20 2020

@author: Laptop Masstel
"""

import os;
check = input("Want to shutdown your computer ? (y/n): ");
if check == 'n':
    exit();
else:
    os.system("shutdown /s /t 1");