
#Stored users:(username,password)

users=[("Admin","2207"),("Shalini","Angel"),("Happy","0722")]

#USer Input
username=input("Enter your name: ")
password=input("Enter your password: ")

#check Login

login_success=False
for user in users:
    if user[0] == username and user[1] == password:
        login_success=True
        break
if login_success:
    print("Login Successful!!")
else:
    print("Login Failed! Wrong username or password")
