import random
from helper_functions import *

def password_generator(check_first_time=True):
    """Function to generate the password and return the password"""
    chars = ("1234567890abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ*&%$#@!")
    if check_first_time:       
        message("You Choose Password Generator" , "yellow")

    message("How many passwords you have to create ? " , "green")
    number_of_password = int(input("➤➤➤   "))
    message("Please Enter Your Password Length" , "green")
    password_length = int(input("➤➤➤   "))
    message("So these are your passwords:-" , "magenta")
    
    for i in range(number_of_password):
        password = ""
        for j in range(password_length):
            password += random.choice(chars)
        message(str(i+1) + '- '+password, "magenta")


def check_satisfaction():
    """Function to check if the user want to continue or not"""

    message("Joko Asking... Are these passwords satisfying for You ?" , "green")
    message("1. Yes 2. No" , "green")
    user = input("➤➤➤   ")

    return user
    

    

if __name__ == "__main__":
    password_generator()
    # after_feature()
    # goodbye()
    # clear()
    # exit()
    # print(password_generator())
    # print(after_feature())
    # print(goodbye())
    # print(clear())
    # print(exit())
    # print(password_generator())
    # print(after_feature())
    # print(goodbye())
    # print(clear())
    # print(exit())
    # print(password_generator())
    # print(after_feature())
    # print(goodbye())
    # print(clear())
    # print(exit())
    # print(password_generator())
    # print(after_feature())
    # print(goodbye())
    # print(clear())
    # print(exit())
    # print(password_generator())
    # print(after_feature())
    # print(goodbye())
    # print(clear())
    # print(exit())
    # print(password_generator())
    # print(after_feature())
    # print(goodbye())
    # print(clear())
    # print(exit())
    # print(password_generator())
    # print(after_feature())
    # print(goodbye())
    # print(clear())
    # print(exit())
    # print(password_generator())
    # print(after_feature())
    # print(goodbye())
    # print(clear())
    # print(exit())
    # print(password_generator())
    # print(after_feature())
    # print(goodbye())
    # print(clear())
    # print(exit())
    # print(password_generator())
    # print(after_feature())
    # print(goodbye())
    # print(clear())
    # print(exit())
    # print(password_generator())
    # print(after_feature())
    # print(goodbye())
    # print(clear())
    # print(exit())
    # print(password_generator())
    # print(after_feature())
    # print(




# try:
    
   
    
    

#     for passw in range(TO_GENERATE+1):
#         print("      or")
#         password = ""
#         for should_apply in range (Length_of_password):
#             password += random.choice(cherecters_for_Genarating_password)
#         print(password)
    
#     print("Are these passwords satisfing you Y/N")
#     satisfing = str(input())
        
#     if satisfing == "Y" or satisfing == "y":
#         print("Ok sir Thanks")
#     elif satisfing == "N" or satisfing == "n":
#         print("So these are your passwords Again:- ")
#         for passw in range(TO_GENERATE):
#             password = ""
#             for should_apply in range (Length_of_password):
#                 password += random.choice(cherecters_for_Genarating_password)
#             print(password)
#     else:
#         print("incorrect input")
# except ValueError:
#     print("Incorrect input Sorry")
