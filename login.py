import os
import time

user_name = open('user.txt')
u_n = user_name.read()
user_pass = open('pass.txt')
u_p = user_pass.read()

print("Welcome",u_n)
passw = input("Enter Password : ")
if passw == u_p:
    print(" Logging in ")
    os.startfile("main.py")

else:
    print("Wrong Password")