import os
import time

os.system("cls")
time.sleep(0.2)
print("""
██████████████████████████████████████████████████████
█─▄▄▄─█▄─▄▄▀█▄─█─▄█▄─▄▄─█─▄─▄─█▄─▄█─▄▄▄─███─▄▄─█─▄▄▄▄█
█─███▀██─▄─▄██▄─▄███─▄▄▄███─████─██─███▀███─██─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▀▄▄▄▄▄▀""")
ask = input("Already Have an account?")
if ask == "yes":
    time.sleep(2)
    os.startfile("login.py")
else:
    user = input("Username [?]")
    password = input("Password [?]")
    f = open('user.txt')
    f.write(user)
    f.close
    f = open('pass.txt')
    f.write(password)
    f.close
