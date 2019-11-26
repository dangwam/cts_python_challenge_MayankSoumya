# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:02:40 2019

@author: MAYANK DANGWAL
"""

class Breed:
   'Common base class for breed'
      
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
      
    # setter method for inserting data into table
   def set_all(self,id,name,temp,coat): 
        #self._id=id
        self._name=name
        self._temp=temp
        self._coat=coat

class Pupper:
    
   'Common base class for pupper'
   breed=Breed()  
   def __init__(self,id,name,sex,weight,height,color,birthdate,breed):
              self.id=id
              self.name=name
              self.sex=sex
              self.weight=weight
              self.height=height
              self.color=color
              self.birthdate=birthdate
              self.breed=breed
     
   # setter method for inserting data into table
   def set_all(self,id,name,sex,weight,height,color,birthdate,breed): 
              #self.id=id
              self.name=name
              self.sex=sex
              self.weight=weight
              self.height=height
              self.color=color
              self.birthdate=birthdate
              self.breed=breed
              