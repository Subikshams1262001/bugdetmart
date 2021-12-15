#!C:/Users/arun/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,cgitb;cgitb.enable()
import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",database="mart")
cur=conn.cursor()
q1="""select max(id) from customer_reg"""
cur.execute(q1)
r=cur.fetchone()
if r[0]!=None:
    n=r[0]
else:
    n=0
z=""
if n<10:
    z="000"
elif n<100:
    z="00"
elif n<1000:
    z="0"
else:
    z=""
custid="customer"+z+str(n+1)
print("""
<html>  
<head>   
<title>Customer registration</title>
<link rel="stylesheet" type="text/css" href="styles/styles1.css">
<link  rel="icon" type="logo/icon" href="images/bmglogo.PNG">
<link rel="stylesheet" type="text/css" href="styles/css/bootstrap.min.css">
<script src="styles/js/jquery.min.js"></script>
<script src="styles/js/bootstrap.min.js"></script>
<style>
body{
background-image: url('images/loginbg4.jpg');
background-size: cover;
background-repeat: no-repeat;
height: 100%;
}
.header{
top:0;
left:0;
height:100px;
width:500%;
position:fixed;
background-color:green;
}
.card{
height: 650px;
margin-top: auto;
margin-bottom: auto;
width: 500px;
background-color: rgba(232,230,232,0.7) !important;

</style>
</head>  
<body> 
<div class="header">
<img src="images/bmglogo.PNG" alt="logo" width="90" height="90"
style="margin-left:5px;
margin-top:4px;
margin-bottom:5px;border-radius:50%">
<div class="google">
<h1 style="margin-left:65px;margin-top:25px;font-family:times new roman;font-size:40">Budget mart grocery system</h1>
 </div>
 </div><br><br><br><br><br>""")
print("""
 <center>
<div class="card"> 

<h3><br><b>REGISTER HERE</b></h3>
<form action="#" method="post" enctype="multipart/form-data" >
<table style="color:black;font-family:Times New Roman;">
<tr>
<td align="left"><b>Customer ID:</b></td>
<td><input type="text" name="custid" id="custid" value="%s" readonly autocomplete="off"></td>
</tr>
<tr>
<td align="left"><b><br>Name:</b></td>
<td><br><input type="text" name="name" id="name" required></td>
</tr>
<tr>
<td align="left"><b><br>DOB:</b></td>
<td><br><input type="date" name="dates" id="dates" required></td>
</tr>
<tr>
<td align="left"><b><br>Gender:</b></td>
<td><br><input type="radio" name="gm" id="mname">Male<input type="radio" name="gm" id="fname">Female</td>
</tr>
<tr>
<td align="left"><b><br>Username:</b></td>"""%(custid))
print("""
<td><br><input type="text" name="uname" id="uname" value="%s" readonly autocomplete="off"></td>
</tr>
<tr>
<td align="left"><b><br>Password:</b></td>

<td><br><input type="password" name="pwd" id="pwd" required></td>
</tr>
<tr>
<td align="left"><b><br>E-mail:</b></td>
<td><br><input type="email" placeholder="@gmail.com" name="gmail" id="gmail" required></td>
</tr>
<tr>
<td align="left"><b><br>Mobile number:</b></td>
<td><br><input type="tel" name="number" id="number" required></td>
</tr>
<tr>
<td align="left"><b><br>Address:</b></td>
<td><br><textarea rows="4" cols="25"  name="address" id="address"></textarea></td>
</tr>
<tr>
<td><b><br>Profile:</b></td>
<td><br><input type="file" id="profile" name="profile"></td>
</tr>
</table><br>
<input type="submit" name="submit" id="submit" value="Register" class="btn float-right login_btn">&nbsp&nbsp&nbsp
<input type="reset" value="Cancel" class="btn float-right login_btn" onclick="location.href='index.html';">
</form>
<a href="customer_login.py"><u><b>Existing user? Click to Login</b></u></a>
</div> 
</center>
</body>  
</html>  
"""%(custid))
f=cgi.FieldStorage()
sub=f.getvalue("submit")
if sub != None:

    customerid=f.getvalue("custid")
    name=f.getvalue("name")
    dob=f.getvalue("dates")
    gender=f.getvalue("gm")
    uname=f.getvalue("uname")
    pwd=f.getvalue("pwd")
    email=f.getvalue("gmail")
    mobno=f.getvalue("number")
    address=f.getvalue("address")
    profile=f['profile']
    if profile.filename:
        import os

        fp=os.path.basename(profile.filename)
        open("images/" + fp, "wb").write(profile.file.read())

        q="""insert into
        customer_reg(custid,name,dates,gm,uname,pwd,gmail,number,address,profile)
        values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(customerid,name,dob,gender,uname,pwd,email,mobno,address,fp)
        cur.execute(q)
        conn.commit()
        conn.close()

        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        mail_content = """Hello,%s
                          Username:%s
                          Password:%s
                        """%(name, uname, pwd)
        sender_address = 'budgetmartproject21@gmail.com'
        sender_pass = 'mart2021'
        receiver_address = email
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Registered Successfully!'
        message.attach(MIMEText(mail_content, 'plain'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()

        print("""
                            <script>
                			alert("Registered successfully");
                            location.href="customer_login.py";
                            </script>
                           """)
    else:
        print("""
                            <script>
                            alert("Login invalid");
                            location.href="customer_reg.py";
                            </script>
                            """)