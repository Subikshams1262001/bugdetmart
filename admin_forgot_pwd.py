#!C:\Users\arun\AppData\Local\Programs\Python\Python39\python.exe
print("Content-type:text/html \r\n\r\n")
import cgi, pymysql, cgitb;cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="mart")
cur = conn.cursor()
print("""
<html lang="en">
<head>
    <title>Forgot password?</title>
    <link  rel="icon" type="logo/icon" href="images/bmglogo.PNG"> 
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
    <meta name="description" content=""/>
    <link rel="stylesheet" href="styles/css/bootstrap.min.css">
    <link rel="stylesheet" href="styles/css/style.css">

<script>
function validate()
{
        var letters = /^[A-Za-z]+$/;
	    var password = /^(?=.[A-Za-z])(?=.\d)(?=.[@$!%#?&])[A-Za-z\d@$!%*#?&]{8,}$/;

  var a=document.getElementById('uname').value;
  var b=document.getElementById('pwd1').value;

	   if(a == "" and b == "")
	   {
	   alert("Enter the username and password");
	   return false;
	   }	   
}
</script>
</head>
<style>

.header1{
height:100px;
width:100%;
position:absolute;
margin-top:0px;
background-color:green;
}

.rel{
color:white;
position:absolute;
top:10%;
margin-left:0px;
font-family:Times New Roman;
}

body {
    background-image: url('images/loginbg.jpg');

}

.login {
    background-color: #fff;
    width: 30%;
    margin: 80px auto;
    border-radius: 10px;
    padding: 20px;
    margin-top:218px;

}

.login>.row>h2 {
    margin: auto;
}

.btn-form {
    width: 100%;
    margin-top: 20px;

}

</style>
<body>

<div>
      <div class="header1">
<img src="images/bmglogo.PNG" alt="logo" width="90" height="90"
style="margin-left:5px;
margin-top:4px;
margin-bottom:5px;border-radius:50%">
<div class="rel">
<h1 style="margin-left:115px;font-size:40;margin-top:15px">Budget mart grocery system</h1>
</div>
</div>
</div>


    <div class="container">
        <div class="login">
            <div class="row">
               <fieldset> <legend>

<h3><center><b>FORGOT PASSWORD?</b>
</center></h3></legend><br>
               <form action="#" method="post" onsubmit="validate()">
                <div class="col-md-12">
                    <label for="username">Enter your Username:</label>
                    <input type="text" class="form-control" id="uname" name="uname" autocomplete="off" required>
                    <br>
                         </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                     <input type="submit" id="submit" value="Get password" name="submit" class="btn btn-primary btn-form">

                </div>
                <div class="col-md-6">
                   <input type="button"  value="cancel"  class="btn btn-primary btn-form" onclick = "location.href ='shopowner_login.py'">
                   </div> 
                   </div><br>

                </div>
</fieldset>
</body>
</html>""")

f = cgi.FieldStorage()
usr = f.getvalue("uname")
v = f.getvalue("submit")
if v != None:

    q = """select pwd from admin where uname='%s'""" % (usr)
    cur.execute(q)
    r = cur.fetchone()
    if r[0] != None:
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        sender_address = 'budgetmartproject21@gmail.com'
        sender_pass = 'mart2021'
        msg = """
      Hi, Welcome %s
      Your password: %s
      """ % (usr, r[0])
        receiver_address = 'aarthikesavan02@gmail.com'
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Forgot password!'
        message.attach(MIMEText(msg, 'plain'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()

        print("""
              <script>
                 alert("Password sent to your mail");
                 location.href="adminlogin.py";

              </script>   
                 """)