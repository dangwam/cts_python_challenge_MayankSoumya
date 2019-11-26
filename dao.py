# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:52:21 2019

@author: MAYANK DANGWAL
"""

import mysql.connector

def read_breed(id):
                    mydb = mysql.connector.connect(
                            host="localhost",
                            user="admin",
                            passwd="admin"
                            )
                    query="""select A.*,B.* from test_schema.breed A .test_schemawhere id=%s"""
                    mycursor = mydb.cursor()
                    mycursor.execute(query,id)
                    myresult = mycursor.fetchall()
                    return myresult
                    mydb.close()

def read_pupper(id):
                    mydb = mysql.connector.connect(
                            host="localhost",
                            user="admin",
                            passwd="admin"
                            )
                    query="""select A.id,A.name,B.name,B.sex,B.weight,B.height,B.color,B.date_of_birth from
                            test_schema.breed A,test_schema.pupper B
                            where A.'%s'=B.'%s'"""
                    mycursor = mydb.cursor()
                    mycursor.execute(query,id)
                    myresult = mycursor.fetchall()
                    return myresult
                    mydb.close()  

     
id=input("enter id::")
my_list = [id]
x=read_breed(my_list)
print("Breed==> :: {}".format(x))
x=read_pupper(my_list)
print("PupperBreed==> :: {}".format(x))