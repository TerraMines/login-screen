import re
import sys
import time
# import keyboard <-- after keyboard installed enable this

def newUser():
    # jiberish
    print("Welcome to the Account Creation Page")
    time.sleep(3)
    print("We just need to get a few details from you")
    time.sleep(3)
    # user input 
    user = str(input("Username: "))
    # user validation
    while not(whiteSpaceCheck(user)) or len(user) > 15:
        print("Username is invalid")
        print("Username should not be more than 15 characters")
        print("Username should not contain spaces inside")
        user = str(input("Username: "))

    # email input
    email = str(input("Email: "))

    # email validation
    while not(domainCheck(email)) or not(whiteSpaceCheck(email)):
        print("Email is invalid")
        print("Username should not contain spaces inside")
        email = str(input("Email: "))

    # password input
    password = str(input("Password: "))

    #password validation
    while not(passwordCheck(password)) or not(whiteSpaceCheck(password)):
        print("Password is invalid")
        print("Password should atleast have 1 Uppercase character")
        print("Password should atleast have 1 Lowercase character")
        print("Password should atleast have 1 Special Symbol")
        print("Password should atleast 1 Digit")
        print("Password should not contain spaces inside")
        password = str(input("Password: "))

    # database entry of all 3 items
    database = open("userdata.txt","a")
    try:
        database.write(f"{user} {email} {password}\n")
        print("Account Succesfully Created!")
    finally:
        database.close()

# Whitespace check
def whiteSpaceCheck(string):
    strippedString = string.strip()
    if " " in strippedString:
        return False
    else:
        return True

# Domain check
def domainCheck(email):
        emailDomains = ["@gmail.com","@yahoo.com","@outlook.com"]
        for domain in emailDomains:
            if email.endswith(domain):
                return True
        return False

# password check function
def passwordCheck(passw):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]).{8,}$"
    
    if re.match(pattern,passw):
        return True
    else:
        return False

def login():
    # user input
    user = str(input("Username or Email: "))
    password = str(input("Password: "))
    validRecord(user,password)

# checking if login details are correct
def validRecord(user,passw):
    # checking if its username or email
    # checkItem = 0 for email, 1 for username
    if domainCheck(user) == True:
        checkItem = 1 
    else: 
        checkItem = 0

    # comparing user data with database records
    database = open("userdata.txt","r")
    
    found = False
    record = database.readline().strip().split(" ") # this line not being here gave me a lot of trouble
    while not found and record[0]!="":
        if user == record[checkItem]:
            found = True
            break

        record = database.readline().strip().split(" ") #yh
        
    
    database.close()

    # password comparing
    if found:
        print("User registered..")
        time.sleep(2.5)
        print("Checking Password..")
        time.sleep(2.5)
        tries = 0
        x = 0
        # looping for password entry tries
        while x < 5:
            if passw != record[2]:
                tries = 5 - x
                x += 1
                print("Password wrong, Try again")
                print(f"{tries} tries left")
                passw = str(input("Password: "))
        
            if passw == record[2]:
                noTry = True
                print("Yay you logged in!")
                break    

        if tries == 1 and not noTry:
            print("SYSTEM LOCKED AFTER TOO MANY TRIES")
            time.sleep(2.5)
            print("Please contact admin to resolve the issue thank you")
            exitProgram()

    else:
        print("User not found...")
        print("Press 1 to register an Account")
        print("Press 2 to try logging again")
        print("Press 0 to go back to main menu")
        opt = int(input("Select an option: "))
        if opt == 1:
            newUser()
        elif opt == 2:
            login()
        elif opt == 0:
            main()
        else:
            exitProgram()

def changePassword():
    print("Changing password isnt available in this version of the program")
    time.sleep(2)
    print("Press 0 to go back to main menu: ")
    opt = str(input())
    if opt == 0:
        main()
    else:
        exitProgram()

def exitProgram():
    print("EXITING....")
    time.sleep(3)
    print("Thank you for your time")
    # keyboard.wait() <-- needs to have the keyboard module installed
    sys.exit()


###########################################################################
# Main function

def main():
    print("The LoginScreen v1.0")
    time.sleep(3)
    print("1. Register as a new user")
    print("2. Login.")
    print("3. Change your password.")
    print("4. Exit.")

    choice = int(input("Please select a menu option: "))

    if choice == 1:
        newUser()
    elif choice == 2:
        login()
    elif choice == 3:
        changePassword()
    elif choice == 4:
        exitProgram()
    else:
        print("Incorrect option. Try again.")

main()
