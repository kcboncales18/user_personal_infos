#this will read the datas 
with open("./user_data.txt", "r") as file:
    lines = file.readlines()
    print(lines)