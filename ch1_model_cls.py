# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:02:40 2019

@author: MAYANK DANGWAL
"""

class Breed:
   'Common base class for all employees'
      
   def __init__(self,id,name,temp,coat):
              self.id=id
              self.name=name
              self.temp=temp
              self.coat=coat
     
        # getter method 
   def get_id(self,id,name,temp,coat): 
        return self._id 
        return self._name
        return self._temp
        return self._coat
      
    # setter method 
   def set_all(self,id,name,temp,coat): 
        self._id=id
        self._name=name
        self._temp=temp
        self._coat=coat

        
        
   def displayInfo(self):
     print ("id : ",self.id,", name :",self.name,", tempremanent : ",self.temp)


