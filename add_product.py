#!C:/Users/arun/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,cgitb;cgitb.enable()
import pymysql

f=cgi.FieldStorage()
id=f.getvalue("id")

conn=pymysql.connect(host="localhost",user="root",password="",database="mart")
cur=conn.cursor()
q2="""select max(id) from add_product"""
cur.execute(q2)
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
pid="product"+z+str(n+1)
q="""select * from shopowner_reg where id=%s"""%(id)
cur.execute(q)
r1=cur.fetchone()
print("""
<html>
<head>
<title>Shopowner dashboard</title>
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
width:88%;
padding-top:0px;
padding-left:20px;
margin-left:-10px;
}
body
{
background-image:url('images/dashbg5.jpg');
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
</style>
<body>
<div class="full">
<div class="container-fluid" class="jumbotron text-left">
<div class="row" style="background-color:green;">
<div class="col-sm-0"><img height="90px" width="90px"
 src="images/bmglogo.PNG" alt="logo"></div>
 <h1 width="100%" class="h1" style="margin-left:20px;margin-top:17px;">Budget mart grocery system</h1></div>
</div>
</div>
""")
print("""
<div class="sidebar">
<div class="row">
<div class="col-2 collapse show d-md-flex pt-0 pl-2 pr-0  min-vh-100"  class="sidebar" >
<ul class="nav flex-column flex-nowrap  overflow-hidden" style="background-color:rgba(0,0,0,0.8)">
<li class="nav-item">
<a class="nav-link collapsed text-truncate" style="width:200px;" href="shopowner_profile.py?id=%s" >
<span class="d-none d-sm-inline" style="color:white;" >PROFILE</span></a></li>
<li class="nav-item">
<a class="nav-link collapsed text-truncate" href="#submenu1" data-toggle="collapse" data-target="#submenu1">
<span class="d-none d-sm-inline" style="color:white;">PRODUCT</span></a>
<div class="collapse" id="submenu1" aria-expanded="false">
<ul class="flex-column pl-2 nav">
<li class="nav-item">
<a class="nav-link py-0" href="add_product.py?id=%s">
<span style="color:blue;"><i>Add</i></span></a></li></ul>
<ul class="flex-column pl-2 nav">
<li class="nav-item">
<a class="nav-link py-0" href="view_product.py?id=%s">
<span style="color:blue;"><i>Existing</i></span></a></li>
</ul>
</div>
</li>
<li class="nav-item">
<a class="nav-link collapsed text-truncate" href="#submenu2" data-toggle="collapse" data-target="#submenu2">
<span class="d-none d-sm-inline" style="color:white;">CUSTOMER ORDER</span></a>
<div class="collapse" id="submenu2" aria-expanded="false">
<ul class="flex-column pl-2 nav">
<li class="nav-item">
<a class="nav-link py-0" href="add_order.py?id=%s">
<span style="color:blue;"><i>Add</i></span></a></li>
</ul>
<ul class="flex-column pl-2 nav">
<li class="nav-item">
<a class="nav-link py-0" href="existing_order.py?id=%s">
<span style="color:blue;"><i>Existing</i></span></a></li>
</ul>
</div></li>
<li class="nav-item">
<a class="nav-link collapsed text-truncate" href="index.html" >
<span class="d-none d-sm-inline" style="color:white;">LOGOUT</span></a></li>
</ul>
</div>"""%(id,id,id,id,id))
print("""
<div class="col-sm-2">
</div>
<div class="col-sm-6"><br>
<tr><h1 style="font-size:30;font-family:algerian"><b>Add product</tr>""")
print("""
<form action="#" method="post" enctype="multipart/form-data" >
<table style="color:black;font-family:Times New Roman;">
<tr>
<td align="left"><b><br>Shop Id:</b></td>
<td><br><input type="text" name="shopid" id="shopid" value="%s" readonly autocomplete="off"></td>
</tr>
<tr>
<td align="left"><b><br>Product Id:</b></td>
<td><br><input type="text" name="pid" id="pid" value="%s" readonly autocomplete="off"></td>
</tr>
<tr>
<td align="left"><b><br>Product Name:</b></td>
<td><br><input type="text" name="product" id="product" required></td>
</tr>
<tr>
<td><b><br>Image:</b></td>
<td><br><input type="file" id="image" name="image"></td>
</tr>
<tr>
<td align="left"><b><br>Quantity(kg):</b></td>
<td><br><input type="text" name="quantity" id="quantity" required></td>
</tr>
<tr>
<td align="left"><b><br>Price:</b></td>
<td><br><input type="text" name="price" id="price" required></td>
</tr>
<tr><td><b><h3><input type="submit" name="submit" id="submit" value="Add" class="btn float-left login_btn" style="margin-left:50px;margin-top:25px;font-family:algerian;"></td>

<td>&nbsp &nbsp &nbsp <input type="reset" value="Cancel" class="btn float-right login_btn" style="margin-right:350px;margin-top:28px;font-family:algerian;"></b></h3></td></tr>
</table>
</form>


</div>
</div>
</div>
</body>
</html> 
"""%(r1[1],pid))

sub=f.getvalue("submit")
if sub != None:

    sid=f.getvalue("shopid")
    pid=f.getvalue("pid")
    productname=f.getvalue("product")
    image=f['image']
    quantity=f.getvalue("quantity")
    price=f.getvalue("price")

    if image.filename:
        import os
        fp=os.path.basename(image.filename)
        open("images/" + fp, "wb").write(image.file.read())

        q1="""insert into add_product(shopid,pid,product,image,quantity,price)values('%s','%s','%s','%s','%s','%s')"""%(sid,pid,productname,fp,quantity,price)
        cur.execute(q1)
        conn.commit()
        conn.close()

        print("""
                            <script>
                			alert("Product added");
                            location.href="view_product.py?id=%s";
                            </script>
                           """%(id))