# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:44:45 2019

@author: MAYANK DANGWAL
"""
import sys
from dao import find_breed
from dao import  find_pupper_breed
from dao import  find_pupper
from dao import find_all_breeds
from dao import  find_pupper_by_breed
from dao import add_breed
from dao import add_pupper
from dao import del_pupper_by_name
from dao import find_pupper_by_field


def one():
#########find_breed(id)
 print("*****************Find Breed by id*************")
 id=input("enter id::")
 my_list = [id]
 x1=find_breed(my_list)
 print("1 Breed==> :: {}".format(x1))

#########find_pupper_breed(id)
def two():
 print("*****************Find Breed of Pupper by id*************")
 id=input("enter id::")
 my_list = [id]
 print("Finding pupper by id equal to {}".format(id))
 x2=find_pupper_breed(my_list)
 print("2 PupperBreed==> :: {}".format(x2))
#########find_pupper(id)
def three():
 print("*****************Find Pupper by id*************")
 id=input("enter id::")
 my_list = [id]
 print("Finding pupper by id equal to {}".format(id))
 x3=find_pupper(my_list)
 print("3 Pupper==> :: {}".format(x3))
#########find_all_breeds()
def four():
 print("*****************Find ALL Breeds*************")
 x4=find_all_breeds()
 print("4 All Breeds==> :: {}".format(x4))
#########find_pupper_by_breed(b)
def five():
 print("*****************Find Pupper by breed*************")
 b=input(" enter breed name ")
 b_list=[b]
 x5=find_pupper_by_breed(b_list)
 print("5 All Pupper Breeds==> :: {}".format(x5))
#########find_pupper_by_field(nme)
def six():
 nme=input("Enter Name to search in pupper")
 x6=find_pupper_by_field(nme)
 print(x6)
 print("7 Pupper search by name complete")
#########add_breed(dd)
def seven():
 print("*****************Add Breed*************")
 try:
  t_name=input("Enter name ::")
  if(t_name==""):
        raise NameError
 except NameError:
       print("Name cannot be blank")
       sys.exit(1)
 t_temp=input("Enter temperament ::")
 t_coat=input("Enter coat ::")
 in_data=(t_name,t_temp,t_coat)
 print(in_data)
 add_breed(in_data)
 print("7 Breed add complete")
#########add_pupper(pp)
def eight():
  try:
     tt=input("Enter values seperated by a comma ::")
     t_name=tt.split(',')
     for ii in t_name:
       if(ii==""):
          raise NameError
  except NameError:
       print("Field cannot be blank {}".format(t_name[ii]))
       sys.exit(1)
  in_data=tuple(t_name)
  print(in_data)
  add_pupper(in_data)
  print("8 Pupper add complete")
#########del_pupper_by_name()
def nine():
 print("Adopt (delete) a Pupper by id. Returns the Pupper deleted or none")
 del_pupper_by_name()
 print("9 Breed delete complete")

def my_main_control(j):
    if (j=="1"):
        one()
    elif (j=="2"):
        two()
    elif (j=="3"):
        three()
    elif (j=="4"):
        four()
    elif (j=="5"):
        five()
    elif (j=="6"):
        six()
    elif (j=="7"):
        seven()
    elif (j=="8"):
        eight()
    elif (j=="9"):
        nine()
    else:
        ("Not a Valid option:: try again")

print("end of program controller")


