import os
import time
print("""

╔═══╦═══╦╗──╔╦═══╦════╦══╦═══╗╔═══╦═══╗
║╔═╗║╔═╗║╚╗╔╝║╔═╗║╔╗╔╗╠╣╠╣╔═╗║║╔═╗║╔═╗║
║║─╚╣╚═╝╠╗╚╝╔╣╚═╝╠╝║║╚╝║║║║─╚╝║║─║║╚══╗
║║─╔╣╔╗╔╝╚╗╔╝║╔══╝─║║──║║║║─╔╗║║─║╠══╗║
║╚═╝║║║╚╗─║║─║║────║║─╔╣╠╣╚═╝║║╚═╝║╚═╝║
╚═══╩╝╚═╝─╚╝─╚╝────╚╝─╚══╩═══╝╚═══╩═══╝""")
print("Options")
print ("Hangman")
print ("Snake")
ask1 = input("What would you like to play? ")
if ask1 == "hangman":
    os.startfile("hang.py")
if ask1 == "snake":
    os.startfile("snake.py")