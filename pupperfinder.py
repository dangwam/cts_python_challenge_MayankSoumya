# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:48:39 2019

@author: MAYANK DANGWAL
"""

from controller import my_main_control

y=input("""
      Choose one of the options from below list. Enter a number for operation
        1).find_breed(id)
        2).find_pupper_breed(id)
        3).find_pupper(id)
        4).find_all_breeds()
        5).find_pupper_by_name
        6).find_pupper_by_field::Enter Name of the Pupper
        7).add_breed(dd)
        8).add_pupper(pp)
        9).del_pupper_by_name()
""")

z=int(y)
if z in range(1,9):
                    my_main_control(y)
else:
    print("Not  a valid option- try again")

