from termcolor import colored
from time import sleep
from random import randint
import time
import os

def message(string , color):
    """Function to print message in color for the user

    Args:
        string (_type_): message to be printed
        color (_type_): color of the message
    """
    welcome = colored(string, color, attrs=['bold'])
    msg = ""
    for l in welcome:
        print(msg, end="\r")
        msg += l
        time.sleep(0.07)
    print()



def welcome():
    """_Say Welcome To The User_"""

    message("Welcome To The Mid-Project" , "cyan")
    message("Hello my friend I'm Joko I will help you to deal with this app" , "cyan")
    message("My App Have Three features You Can Choose One Of Them" , "cyan")
    clear()

def start_choose():
    """Function to choose the feature of the app and return the number of the feature"""

    message("Please Choose One Of The Following Features" , "yellow")
    message("1.Email Slicer  2.Password Generator 3.Website Blocker 4. Exit" , "green")
    user = input("➤➤➤   ")
    return user

def after_feature():
    """function that check if the user want to continue or not"""

    clear()
    message('choose if you want to continue or leave', 'green')
    message('1. Continue 2.Exit', 'green')
    user = input('➤➤➤   ')
    if user == '1':
        start_choose()
    elif user == '2':
        goodbye()


def goodbye():
    """_Say Good Bye For The User_"""

    message('Thank You For Using My App', 'cyan')
    message('Good Bye', 'red')
    clear()
    message("Joko Says Let's See You Next Time" , "grey")


def clear():
    """Function to clear the screen"""

    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

