with open("./user_data.txt", "a") as file:
    personal_info = []

    def user_name():     #user's full name
        first_name = input("What is your first name? ")
        middle_name = input("What is your middle name? ")
        surname = input("what is your surname? ")
        file.write(f"\nUser's name is: {first_name} {middle_name} {surname}")

    user_name ()

    def user_age():     #user's ages 
        age = int(input("Ok, how old are you now? "))
        file.write(f"\nUser's age is: {age} years old.")

    user_age()

    def user_birth():   #user's birthday
        month = input("What month are you born? ")
        date = int(input("What is the date of your birthday? "))
        year = int(input("and what year are you born? "))
        file.write(f"\nUser's birthday is on: {month}, {date} {year}")

    user_birth()

    def user_gender():  #user's sex
        sex = input("Are you a male or female? ")
        file.write(f"\nUser's sex is:{sex}")        

    user_gender()

    def user_address(): #user's address
        barangay = input("What barangay your place in? ")
        municipality = input("What municipality your place in? ")
        province = input("What province your place in? ")
        country = input("What country do you live? ")
        file.write(f"\nUser lived at: {barangay}, {municipality}, {province}, {country}")     

    user_address()

    def user_nationality(): #user's nationality 
        citizenship = input("What is your nationality: ")
        file.write(f"\nUser's nationality is:{citizenship}")

    user_nationality()

    def user_religion(): #religion of the user
        religion = input("What religion do you belong to? ")
        file.write(f"\nUser's religion is: {religion}")   

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
    
        #uhh it ask user twice for information before it asks this yes or no question
        retry = input("do you want to enter another entry? Yes or no. ").lower()
        if retry == "no":
            break