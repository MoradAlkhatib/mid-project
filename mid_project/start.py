from helper_functions import *
from email_slicer import *
from password_generator import *


# welcome()
user = start_choose()

if user == "1":
    email_slicer()
    after_feature()
    
elif user == "2":
    password_generator()

    def checker():
        user = check_satisfaction()
        if user == "1":
            after_feature()
        elif user == "2":
            password_generator(False)
            checker()
    checker()
           

elif user == "3":
    message("Thank You For Using My App" , "cyan")
    message("Good Bye" , "cyan")
elif user == "4":
    goodbye()
    




