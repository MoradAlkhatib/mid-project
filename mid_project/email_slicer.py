from helper_functions import message


def email_slicer():
    """Function to slice the email and return the sliced email"""

    message("You Choose Email Slicer" , "yellow")
    message("Please Enter Your Email" , "green")
    email = input("➤➤➤   ").strip()
    email_slicer = email.split("@")
    user_name  = email_slicer[0]
    domain = email_slicer[1]
    message("Your User Name Is : " + user_name , "magenta")
    message("Your Domain Is : " + domain , "magenta") 
    



    
