#this will read the datas 
with open("./user_data.txt", "r") as file:
    user_infos = file.readlines()
for lines in user_infos:
    print(lines)