# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:52:21 2019
macgabhain
@author: MAYANK DANGWAL
"""
import sys
import mysql.connector
from model import Breed
from model import Pupper
#1==> Find a breed by ID
def find_breed(id):
                    mydb = mysql.connector.connect(
                            host="localhost",
                            user="admin",
                            passwd="admin",
                            database="test_schema"
                            )
                    query="""select * from test_schema.breed where id=%s"""
                    mycursor = mydb.cursor()
                    mycursor.execute(query,id)
                    myresult = mycursor.fetchall()
                    return myresult
                    mydb.close()
#2==> Find Pupper by ID
def find_pupper_breed(id):
                    mydb = mysql.connector.connect(
                            host="localhost",
                            user="admin",
                            passwd="admin",
                            database="test_schema"
                            )
                    query="select A.id,A.name,B.name,B.sex,B.weight,B.height,B.color,B.date_of_birth from test_schema.breed A,test_schema.pupper B where A.id=B.breed_id and B.id = %s"
                    #idstr=[str(id)]
                    mycursor = mydb.cursor()
                    mycursor.execute(query,id)
                    myresult = mycursor.fetchall()
                    return myresult
                    mydb.close()  
#3==>Find all puppers
def find_pupper(id):
                    mydb = mysql.connector.connect(
                            host="localhost",
                            user="admin",
                            passwd="admin",
                            database="test_schema"
                            )
                    query="""select * from test_schema.pupper where breed_id=%s"""
                    mycursor = mydb.cursor()
                    mycursor.execute(query,id)
                    myresult = mycursor.fetchall()
                    return myresult
                    mydb.close()

                    
#4==>Find all breeds
def find_all_breeds():
                    mydb = mysql.connector.connect(
                            host="localhost",
                            user="admin",
                            passwd="admin",
                            database="test_schema"
                            )
                    query="""select * from test_schema.breed"""
                    mycursor = mydb.cursor()
                    mycursor.execute(query)
                    myresult = mycursor.fetchall()
                    return myresult
                    mydb.close()
                    
#5==>Find all Puppers by breed name
def find_pupper_by_breed(b):
                    mydb = mysql.connector.connect(
                            host="localhost",
                            user="admin",
                            passwd="admin",
                            database="test_schema"
                            )
                    query="""select * from test_schema.pupper where name=%s"""
                    mycursor = mydb.cursor()
                    mycursor.execute(query,b)
                    myresult = mycursor.fetchall()
                    return myresult
                    mydb.close()
                    
#6
"""
Search Puppers by multiple parameters (support whichever you like). 
Accepts a map of parameter-value pairs. 
Can be equality or inequality (e.g. sex: F, weightMax: 15 lbs.)
"""
def find_pupper_by_field(nme):
                    mydb = mysql.connector.connect(
                            host="localhost",
                            user="admin",
                            passwd="admin",
                            database="test_schema"
                            )
                    dct={"name1":""}
                    dct["name1"]=nme
                    format_str = """select * from test_schema.pupper where name = ("{a}");"""
                    query = format_str.format(a=dct["name1"])
                    mycursor = mydb.cursor()
                    mycursor.execute(query)
                    myresult = mycursor.fetchall()
                    return myresult
                    mydb.close()


#7 ==>
"""
Add breed to database. (parameter: breed object without ID, no return) 
Missing breed name raises an exception without writing to the database.
"""
def add_breed(dd):
  try:                
    mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="admin",
                            database="test_schema"
                            )
    mycursor = mydb.cursor()
    data = [dd]
    for i in data:
            format_str = """INSERT INTO breed (id,name,temperament,coat)
            VALUES (NULL,"{nm}","{temp}","{ct}");"""
            sql_command = format_str.format(nm=i[0],temp=i[1],ct=i[2])
    print(sql_command)
    mycursor.execute(sql_command)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    mycursor.close()
    mydb.close()                   
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
  except mysql.DataError as e:
    print("DataError")
    print(e)
  except mysql.InternalError as e:
    print("InternalError")
    print(e)
  except mysql.IntegrityError as e:
    print("IntegrityError")
    print(e)
  except mysql.OperationalError as e:
    print("OperationalError")
    print(e)
  except mysql.NotSupportedError as e:
    print("NotSupportedError")
    print(e)
  except mysql.ProgrammingError as e:
    print("ProgrammingError")
    print(e)
  except :
    print("Unknown error occurred")

#8==>
"""
Add Pupper to the database. Breed must exist in the database already.
Exception for bad breed or missing name, sex, or breed

"""
def add_pupper(pp):
  try:                
    mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="admin",
                            database="test_schema"
                            )
    datap = [pp]
    print(datap)
    bb=pp[6]
    breed_id=[bb]
    print("breed_id is ==>{}".format(breed_id))
    mycursor1 = mydb.cursor()
    mycursor = mydb.cursor()
    query1="""select * from test_schema.breed where id=%s"""
#    print(query1)
    mycursor1.execute(query1,breed_id)
    myresult = mycursor1.fetchall()
    print(myresult)
    if (myresult !=""):
        for i in datap:
            format_str = """INSERT INTO pupper (name, sex, weight, height, color, date_of_birth, breed_id)
            VALUES ("{a}","{b}","{c}","{d}","{e}","{f}","{bid}");"""
            sql_command = format_str.format(a=i[0],b=i[1],c=i[2],d=i[3],e=i[4],f=i[5],bid=i[6])
        
        print(sql_command)
        mycursor.execute(sql_command)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    else:
        print("Breed id not found in Breed. Hence no insert made in pauper")
        
    mycursor.close()
    mycursor1.close()
    mydb.close()                 
               
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

#9 ==>Adopt (delete) a Pupper by id. Returns the Pupper deleted or none.
def del_pupper_by_name():
                    d=input(" enter id to delete ")
                    i=tuple(d,)
                    mydb = mysql.connector.connect(
                            host="localhost",
                            user="admin",
                            passwd="admin",
                            database="test_schema"
                            )
                    format_str = """delete from pupper where id = ("{a}");"""
                    query = format_str.format(a=i[0])
                    print(query)
                    mycursor = mydb.cursor()
                    mycursor.execute(query)
                    print(mycursor.rowcount, "record(s) deleted")
                    mydb.commit()
                    mycursor.close()
                    mydb.close()


