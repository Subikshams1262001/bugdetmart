#!C:/Users/arun/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,cgitb;cgitb.enable()
import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",database="mart")
cur=conn.cursor()
f=cgi.FieldStorage()

if len(f)==2:
    id = f.getvalue("id")
    cid = f.getvalue("cid")
else:
    id = f.getvalue("id")
    cid = f.getvalue("cid")
    shopownerid = f.getvalue("shopid")
    name = f.getvalue("name")
    uname = f.getvalue("uname")
    pwd = f.getvalue("pwd")
    email = f.getvalue("gmail")
    mobno = f.getvalue("number")
    address=f.getvalue("address")
    profile = f['profile']
    if profile.filename:
        import os

        fp = os.path.basename(profile.filename)
        open("images/" + fp, "wb").write(profile.file.read())

        q1 = """update shopowner_reg set  shopid='%s',name='%s',uname='%s',pwd='%s',gmail='%s',number='%s',address='%s',profile='%s' where id='%s'
            """%(shopownerid, name, uname, pwd, email, mobno,address, fp,cid)
        cur.execute(q1)
        conn.commit()
        print("""
                        <script>
                        alert("profile updated")
                        location.href="shopowner_profile.py?id=%s";
                        </script>
                """ % (id))
    else:
        q1 = """update shopowner_reg set  shopid='%s',name='%s',uname='%s',pwd='%s',gmail='%s',number='%s',address='%s' where id='%s'
                    """ % (shopownerid, name, uname, pwd, email, mobno, address, cid)
        cur.execute(q1)
        conn.commit()
        print("""
                                <script>
                                alert("profile updated")
                                location.href="shopowner_profile.py?id=%s";
                                </script>
                        """ % (id))
q="""select * from shopowner_reg where id=%s"""%(id)
cur.execute(q)
r=cur.fetchone()
print("""
<html>
<head>
<title>Shopowner dashboard</title>
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
.card{
height: 770px;
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
<a class="nav-link py-0" href="existing_product.py?id=%s">
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
<div class="card">
<h3 style="font-size:30;font-family:algerian"><br><b>Shopowner profile edit</b></h3><br>
<form action="shopowner_profile_edit.py" method="post" enctype="multipart/form-data" >
<input type="hidden" name="id" value="%s">
<input type="hidden" name="cid" value="%s">
<table style="color:black;font-family:Times New Roman;margin-left:-100px;">
<img src="images/%s" width="150" height="150" style="margin-left:150px;">
<tr>
<td align="right"><b><br>Profile:</b></td>
<td><br><input type="file" id="profile" name="profile"></td>
</tr>
<tr>
<td align="right"><b><br>Shopowner ID:</b></td>
<td><br><input type="text" name="shopid" id="shopid" value="%s" readonly autocomplete="off"></td>
</tr>
<tr>
<td align="right"><b><br>Name:</b></td>
<td><br><input type="text" name="name" id="name" value="%s" required></td>
</tr>
<tr>
<td align="right"><b><br>Username:</b></td>
<td><br><input type="text" name="uname" id="uname" value="%s" readonly autocomplete="off"></td>
</tr>
<tr>
<td align="right"><b><br>Password:</b></td>
<td><br><input type="password" name="pwd" id="pwd" value="%s" required></td>
</tr>
<tr>
<td align="right"><b><br>E-mail:</b></td>
<td><br><input type="email" placeholder="@gmail.com" name="gmail" id="gmail" value="%s" required></td>
</tr>
<tr>
<td align="right"><b><br>Mobile number:</b></td>
<td><br><input type="tel" name="number" id="number" value="%s" required></td>
</tr>
<tr>
<td align="right"><b><br>Address:</b></td>
<td><br><textarea rows="4" cols="25"  name="address" id="address" value="%s"></textarea></td>
</tr>
<br>
<tr><td><br><input type="submit" name="submit" id="submit" value="Update" class="btn float-left login_btn" style="margin-left:150px;margin-bottom:-15px;"></td>
<td><input type="reset" value="Cancel" class="btn float-right login_btn" style="margin-left:100px;margin-top:30px;"></td></tr>
</table>
</form>

</div>
</div>
</div>
</div>"""%(id,cid,r[10],r[1],r[2],r[5],r[6],r[7],r[8],r[9]))
conn.close()
print("""
</body>
</html>
""")
