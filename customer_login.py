#!C:/Users/arun/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi, pymysql, cgitb;cgitb.enable()
print("""
<html>
<head>
	<title>Customer login</title>
	<style>
	body{
background-image: url('images/loginbg1.jpg');
background-size: cover;
background-repeat: no-repeat;
height: 100%;
}
	</style>
	<!--Bootsrap 4 CDN-->
	<link rel="stylesheet" href="styles/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <link  rel="icon" type="logo/icon" href="images/bmglogo.PNG">
    <!--Fontawesome CDN-->
	<link rel="stylesheet" href="styles/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">
    <link href="styles/bootstrap1.min.css" rel="stylesheet" id="bootstrap-css">
<script src="styles/bootstrap.min.js"></script>
<script src="styles/jquery.min.js"></script>
	<!--Custom styles-->
	<link rel="stylesheet" type="text/css" href="styles/stylesheet.css">
</head>
<body>
<div class="header" style="height:100px">
<img src="images/bmglogo.PNG" alt="logo" width="90" height="90"
style="margin-left:5px;
margin-top:4px;
margin-bottom:5px;">
<div class="google">
<h1 style="margin-left:65px;font-family:Times New Roman;">Budget mart grocery system</h1>
 </div>
 </div>
<div class="container">
	<div class="d-flex justify-content-center h-100">
		<div class="card" style="height:350px;">
			<div class="card-header">
				<h3>Customer Login</h3>
			</div>
			<div class="card-body">
				<form action="#" method="post">
					<div class="input-group form-group">
						<div class="input-group-prepend">
							<span class="input-group-text"><i class="fas fa-user"></i></span>
						</div>
						<input type="text" name="uname" id="uname" class="form-control" placeholder="username">
						
					</div>
					<div class="input-group form-group">
						<div class="input-group-prepend">
							<span class="input-group-text"><i class="fas fa-key"></i></span>
						</div>
						<input type="password" name="pwd" id="pwd" class="form-control" placeholder="password">
					</div>
					<div class="form-group">
						<input type="submit" name="submit" value="Login" class="btn float-left login_btn" style="margin-left:70px;">&nbsp &nbsp &nbsp
						<input type="reset" name="Cancel" value="Cancel" class="btn login_btn " onclick="location.href='index.html';">
					</div>
				</form>
			</div>
			<div class="card-footer">
				<div class="d-flex justify-content-center links">
					Don't have an account?<a href="customer_reg.py">Create new account</a>
				</div>
				<div class="d-flex justify-content-center">
					<a href="customer_forgot_pwd.py">Forgot your password?</a>
				</div>
			</div>
		</div>
	</div>
</div>
</body>
</html>
""")
conn = pymysql.connect(host="localhost", user="root", password="", database="mart")
cur = conn.cursor()
f = cgi.FieldStorage()
usr = f.getvalue("uname")
psw = f.getvalue("pwd")
v = f.getvalue("submit")
if v != None:

    q = """select id from customer_reg where uname='%s' and pwd='%s'"""%(usr, psw)
    cur.execute(q)
    r = cur.fetchone()
    if r != None:
        print("""
                    <script>
        			alert("login successful");
                    location.href="customer_dashboard.py?id=%s";
                    </script>
                """%(r[0]))
    else:
        print("""
                    <script>
                    alert("Login invalid");
                    location.href="customer_login.py";
                    </script>
                """)