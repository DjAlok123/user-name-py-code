import time
import os

clear = lambda: os. system('clear')

un = input("Enter your username: ")

if un == "git":
    print("Entering to your username")
    time.sleep(2)
san_pas = input("Enter your password: ")

if san_pas == "git":
    print("You are successfully entered your desktop")

else:
    clear()
    print("Exiting Program!")
    time.sleep(3)
    input("Press enter to continue")
