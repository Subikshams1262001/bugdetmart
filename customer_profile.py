#!C:/Users/arun/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,cgitb;cgitb.enable()
import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",database="mart")
cur=conn.cursor()
f=cgi.FieldStorage()
id=f.getvalue("id")
q="""select * from customer_reg where id=%s"""%(id)
cur.execute(q)
r=cur.fetchone()
print("""
<html>
<head>
<title>Customer dashboard</title>
<link rel="stylesheet" type="text/css" href="styles/styles1.css">
<link rel="stylesheet" type="text/css" href="styles/css/bootstrap.min.css">
<link  rel="icon" type="logo/icon" href="images/bmglogo.PNG">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="styles/style.css">
</head>
<script src="styles/styles/js/jquery.min.js"></script>
<script src="styles/styles/js/bootstrap.min.js"></script>
<style>
.h1{
top:0;
font-family:times new roman;
color:white;
font-size:40;
left:30px;
}
.sidebar{
height:100%;
width:90%;
padding-top:0px;
padding-left:20px;
margin-left:-10px;
}
body
{
background-image:url('images/dashbg6.jpg');
background-repeat:no-repeat;
background-size:cover;
}
img{
border-radius:50%;
margin-left:5px;
margin-top:4px;
margin-bottom:5px;
}
</style>
<body>
<div class="full">
<div class="container-fluid" class="jumbotron text-left">
<div class="row" style="background-color:green;">
<div class="col-sm-0"><img height="90px" width="90px"
 src="images/bmglogo.PNG" alt="logo"></div>
 <h1 width="100%" class="h1" style="margin-left:20px;margin-top:17px;">Budget mart grocery system</h1></div>
</div>
</div>""")
print("""
<div class="sidebar">
<div class="row">
<div class="col-2 collapse show d-md-flex pt-0 pl-0 pr-0  min-vh-100"  class="sidebar" >
<ul class="nav flex-column flex-nowrap  overflow-hidden" style="background-color:rgba(0,0,0,0.8)">
<li class="nav-item">
<a class="nav-link collapsed text-truncate" href="customer_profile.py?id=%s" style="width:200px;">
<span class="d-none d-sm-inline" style="color:white;" >PROFILE</span></a></li>
<li class="nav-item">
<a class="nav-link collapsed text-truncate" href="#submenu1" data-toggle="collapse" data-target="#submenu1">
<span class="d-none d-sm-inline" style="color:white;">PURCHASE</span></a>
<div class="collapse" id="submenu1" aria-expanded="false">
<ul class="flex-column pl-2 nav">
<li class="nav-item">
<a class="nav-link py-0" href="add_purchase.py?id=%s">
<span style="color:blue;"><i>Add</i></span></a></li></ul>
<ul class="flex-column pl-2 nav">
<li class="nav-item">
<a class="nav-link py-0" href="existing_purchase.py?id=%s">
<span style="color:blue;"><i>Existing</i></span></a></li>
</ul>
</div>
</li>
<li class="nav-item">
<a class="nav-link collapsed text-truncate" href="index.html">
<span class="d-none d-sm-inline" style="color:white;">LOGOUT</span></a></li>
</ul>
</div>"""%(id,id,id))
print("""
<div class="col-sm-2">
</div>
<div class="col-sm-6"><br><br>
<div> 
<tr><b><h2 style="font-size:30;font-family:algerian">Welcome <td> %s </b></h2></td></tr>
<tr><td><img src="images/%s" width="150" height="150" class="rounded-circle"></td></tr><br>
<tr><td><b>Customer Id:</b></td><td>%s</td></tr><br>
<tr><td><b>Name:</b></td><td>%s</td></tr><br>
<tr><td><b>Email-id:</b></td><td>%s</td></tr><br>
<tr><td><b>Mobile number:</b></td><td>%s</td></tr><br>
<tr><td><b>Address:</b></td><td>%s</td></tr><br>
<tr><td><b>Username:</b></td><td>%s</td></tr><br>
<tr><td><b>Password:</b></td><td>%s</td></tr><br>
<tr><td><a href="customer_profile_edit.py?cid=%s&id=%s"><u>Profile change</u></a></td></tr>
</div>
"""%(r[2],r[10],r[1],r[2],r[7],r[8],r[9],r[5],r[6],r[0],id))
print("""
</div>
</div>
</div>
</body>
</html>
""")