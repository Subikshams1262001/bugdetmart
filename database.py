#!C:\Users\arun\AppData\Local\Programs\Python\Python39\python.exe
print("Content-type:text/html \r\n\r\n")
import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",database="")
cur=conn.cursor()
s="""create database budgetmart"""
cur.execute(s)
conn.commit()
conn.close()
print("success")