personal_info = []

def user_name ():
    first_name = input("What is your first name? ")
    middle_name = input("What is your middle name?")
    surname = input("what is your surname? ")
    fullname = first_name + middle_name + surname
    print("User's name is: ", fullname)
user_name ()
