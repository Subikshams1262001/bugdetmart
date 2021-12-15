#!C:\Users\arun\AppData\Local\Programs\Python\Python39\python.exe
print("Content-type:text/html \r\n\r\n")
import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",database="mart")
cur=conn.cursor()
s="""create table admin(id int(5) auto_increment primary key,uname varchar(20),pwd varchar(20))"""
cur.execute(s)
conn.commit()
conn.close()
print("success")