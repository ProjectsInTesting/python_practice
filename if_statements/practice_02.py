db_username = "Admin"
db_password = "Password"

username = input ("Enter your username: ")
password = input ("Enter the Password:")

if username == db_username and password == db_password:
    print (" You loged in successfully!")
elif username == db_username and password != db_password:
    print ("Incorrect password!  Please try again.")
elif username != db_username and  password == db_password:
    print ("Incorrect username! please try again.")
else:    
    print ("wrong username or password!")
    exit()    