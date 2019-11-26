# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:48:39 2019

@author: MAYANK DANGWAL
"""

from controller import db_read

y=input("Enter operation- read/write ::")

if (y=="read"):
    data1=db_read()
    print("Return Value is :: {}".format(data1))