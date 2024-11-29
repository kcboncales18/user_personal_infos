personal_info = []

def user_name ():     #user's full name
    first_name = input("What is your first name? ")
    middle_name = input("What is your middle name? ")
    surname = input("what is your surname? ")
    print(f"User's name is: {first_name} {middle_name}. {surname}")
user_name ()

def user_age ():     #user's age 
    age = int(input("Ok, how old are you now? "))
    print(f"User's age is: {age} years old. ")
user_age()

def user_birth ():   #user's birthday
    month = input("What month are you born? ")
    date = int(input("What is the date of your birthday? "))
    year = int(input("and what year are you born? "))
    print(f"User's birthday is on: {month}, {date} {year}")
user_birth()