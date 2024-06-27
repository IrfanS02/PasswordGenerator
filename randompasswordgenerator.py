import random
print("Welcome to Random Password Generator: ")
passchar="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123567890!@#$%&*"
noofpass=int(input("Enter the number of password you needed: "))
passlen=int(input("Enter the number of length of password: "))
print("Here you Random passwords are:")
for i in range(noofpass):
    pwd=""
    for ch in range(passlen):
        pwd = pwd + random.choice(passchar)
    print(pwd)
print("----------> THANK YOU <----------")