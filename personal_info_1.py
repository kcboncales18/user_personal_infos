personal_info = []

def user_name():     #user's full name
    first_name = input("What is your first name? ")
    middle_name = input("What is your middle name? ")
    surname = input("what is your surname? ")
    print(f"User's name is: {first_name} {middle_name}. {surname}")
user_name ()

def user_age():     #user's age 
    age = int(input("Ok, how old are you now? "))
    print(f"User's age is: {age} years old. ")
user_age()

def user_birth():   #user's birthday
    month = input("What month are you born? ")
    date = int(input("What is the date of your birthday? "))
    year = int(input("and what year are you born? "))
    print(f"User's birthday is on: {month}, {date} {year}")
user_birth()

def user_gender():  #user's sex
    sex = input("Are you a male or female? ")
    print("User's sex is: ", sex)
user_gender()

def user_address():
    barangay = input("What barangay your place in? ")
    municipality = input("What municipality your place in? ")
    province = input("What province your place in? ")
    print(f"User lived at: {barangay}, {municipality}, {province}")
user_address()

def user_nationality(): #user's nationality 
    citizenship = input("What is your nationality: ")
    print("User's nationality is:  ", citizenship)
user_nationality()

def user_religion(): #religion of the user
    religion = input("What religion do you belong to? ")
    print("User's religion is: ", religion)
user_religion()

while True:         #the program continues to ask         
    full_name = user_name()
    age = user_age()
    birthdate = user_birth()
    sex = user_gender()
    address = user_address()
    citizenship = user_nationality()
    religion = user_religion()
    
    personal_info.append({"user_name":full_name,
                          "user_age":age, 
                          "user_birth": birthdate, 
                          "user_gender":sex,
                          "user_address": address,
                          "user_nationality":citizenship,
                          "user_religion": religion})
    
