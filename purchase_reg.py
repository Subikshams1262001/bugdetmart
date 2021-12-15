#!C:/Users/arun/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,cgitb;cgitb.enable()
import pymysql
from datetime import date

conn=pymysql.connect(host="localhost",user="root",password="",database="mart")
cur=conn.cursor()

tdate=date.today()
f=cgi.FieldStorage()
id=f.getvalue("id")
sid=f.getvalue("sid")

q="""select * from customer_reg where id=%s"""%(id)
cur.execute(q)
r=cur.fetchone()

q1="""select * from add_product where id=%s"""%(sid)
cur.execute(q1)
r1=cur.fetchone()

sub=f.getvalue("submit")

if sub!=None:

    quantity=f.getvalue("quan")
    totalamt=f.getvalue("totalamt")
    paymode=f.getvalue("paymode")

    q="""insert into purchase_reg(sid,pid,custid,quan,paymode,req_date,price,totalamt,image,product,accept)
         values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(r1[1],r1[2],r[1],quantity,paymode,tdate,r1[6],totalamt,r1[4],r1[3],"New")
    cur.execute(q)
    conn.commit()
    conn.close()
    print("""
           <script>
           alert("Your order is received");
           location.href="existing_purchase.py?id=%s";
           </script>
          """)
print("""
<html>
<head>
<title>Customer dashboard</title>
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
.login_btn{
color: black;
background-color: #FFC312;
width: 100px;
}
.login_btn:hover{
color: black;
background-color: white;
}
.card{
height: 270px;
margin-top: auto;
margin-bottom: auto;
width: 500px;
background-color: rgba(232,230,232,0.7) !important;
padding-left:30px;

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
<div class="col-sm-6"><br>
<div class="card">
<h1 style="font-size:30;font-family:algerian"><b>Purchase</b></h1>""")
print("""

<form action="purchase_reg.py" method="post" enctype="multipart/form-data" >
<table style="color:black;font-family:Times New Roman;">
<input type="hidden" name="id" value="%s">
<input type="hidden" name="sid" value="%s">
<input type="hidden" name="price" value="%s">
<tr>
<td align="left"><b><br>Quantity(kg):</b></td>
<td><br><input type="text" name="quan" id="quan"  required autocomplete="off"></td>
</tr>
<tr>
<td align="left"><b><br>Total Amount:</b></td>
<td><br><input type="text" name="totalamt" id="totalamt" required autocomplete="off"/></td>
</tr>
<tr>            
<td align="left"><br><b>Mode of payment:</b></td>
<td>
<br><select name="paymode" id="paymode" required >
<option>Cash on delivery</option>
<option>Card</option>
</td>
</select>
</tr>
<tr><td>
<b><input type="submit" name="submit" id="submit" value="Add" class="btn float-left login_btn" style="margin-left:50px;margin-top:40px;font-family:algerian;"></td>
<td>&nbsp &nbsp &nbsp <input type="reset" value="Cancel" class="btn float-right login_btn" style="margin-right:350px;margin-top:20px;font-family:algerian;"></b></td></tr>
</table>
</form>
</div>
</div>
</div>
</div>
</body>
</html> 
"""%(id,sid,r1[6]))

