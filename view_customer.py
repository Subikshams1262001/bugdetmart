#!C:/Users/arun/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,cgitb;cgitb.enable()
import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",database="mart")
cur=conn.cursor()
f=cgi.FieldStorage()
id=f.getvalue("id")
q="""select * from customer_reg """
cur.execute(q)
r=cur.fetchall()
cnt=0

print("""
<html>
<head>
<title>Admin dashboard</title>
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
width:100%;
padding-top:0px;
padding-left:20px;
margin-left:-10px;
}
body
{
background-image:url('images/dashbg10.jpg');
background-repeat:no-repeat;
background-size:cover;
}
img{
border-radius:50%;
margin-left:5px;
margin-top:4px;
margin-bottom:5px;
}
table,th,td
{
border-collapse:collapse;
border:2px solid black;
padding:10px;
}
</style>
<body>
<div class="full">
<div class="container-fluid" class="jumbotron text-left">
<div class="row" style="background-color:green;">
<div class="col-sm-0"><img height="90px" width="90px"
 src="images/bmglogo.PNG" alt="logo" ></div>
 <h1 width="100%" class="h1" style="margin-left:20px;margin-top:17px;">Budget mart grocery system</h1></div>
</div>
</div>""")
print("""
<div class="sidebar">
<div class="row">
<div class="col-2 collapse show d-md-flex pt-0 pl-2 pr-0  min-vh-100"  class="sidebar" >
<ul class="nav flex-column flex-nowrap  overflow-hidden" style="background-color:rgba(0,0,0,0.8)">
<li class="nav-item">
<a class="nav-link collapsed text-truncate" style="width:200px;" href="#submenu1" data-toggle="collapse" data-target="#submenu1">
<span class="d-none d-sm-inline" style="color:white;" >SUPERMARKET</span></a>
<div class="collapse" id="submenu1" aria-expanded="false">
<ul class="flex-column pl-2 nav">
<li class="nav-item">
<a class="nav-link py-0" href="new_supermarket.py">
<span style="color:blue;"><i>Add</i></span></a></li></ul>
<ul class="flex-column pl-2 nav">
<li class="nav-item">
<a class="nav-link py-0" href="existing_supermarket.py">
<span style="color:blue;"><i>Existing</i></span></a></li>
</ul>
</div>
</li>
<li class="nav-item">
<a class="nav-link collapsed text-truncate" href="#submenu2" data-toggle="collapse" data-target="#submenu2">
<span class="d-none d-sm-inline" style="color:white;">CUSTOMER</span></a>
<div class="collapse" id="submenu2" aria-expanded="false">
<ul class="flex-column pl-2 nav">
<li class="nav-item">
<a class="nav-link py-0" href="view_customer.py">
<span style="color:blue;"><i>View</i></span></a></li>
</ul>
</div></li>
<li class="nav-item">
<a class="nav-link collapsed text-truncate" href="index.html">
<span class="d-none d-sm-inline" style="color:white;">LOGOUT</span></a></li>
</ul>
</div>""")
print("""
<div class="col-sm-2">
<br>
<h2 style="font-size:25;font-family:times new roman"><b>CUSTOMER</b></h2>
<table border="2" width = "100" >
<tr>
<th>S.No</th>
<th>Shop Id</th>
<th>Name</th>
<th>Username</th>
<th>Password</th>
<th>Email</th>
<th>Phone Number</th>
<th>Address</th>
<th>Profile</th>
</tr>""")
for i in r:
    cnt= cnt+1
    print("""
    <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td><img src ="images/%s" width="50" height="50" class="rounded-circle"></td>
    </tr>
    """%(cnt,i[1],i[2],i[5],i[6],i[7],i[8],i[9],i[10]))
print("""
</table>
</div>
</div>
</body>
</html>
""")