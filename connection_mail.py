#!C:/Users/arun/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import smtplib
sender="budgetmartproject21@gmail.com"
password="mart2021"
name="priya"
msg="""WELCOME %s"""%(name)
receiver="aarthikesavan02@gmail.com"
server=smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, msg)
server.quit()
print("success")