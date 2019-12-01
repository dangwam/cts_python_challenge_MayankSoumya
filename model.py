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
     
# setter method for setting all attributes except id
   def set_breed(self,name,temp,coat): 
#       self._id=id
        self.name=name
        self.temp=temp
        self.coat=coat

breed=Breed(0,"","","")
print (breed)
class Pupper:
     
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
   def set_pupper(self,name,sex,weight,height,color,birthdate,breed): 
              #self.id=id
              self.name=name
              self.sex=sex
              self.weight=weight
              self.height=height
              self.color=color
              self.birthdate=birthdate
              self.breed=breed
              