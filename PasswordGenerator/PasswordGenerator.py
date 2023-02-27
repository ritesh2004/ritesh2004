###### This is a password generator which creates strong passwords that you can stay safe ######
###### Author :- Ritesh Pramanik ######
import string
import random
print("Welcome to my Password Generator! This is a password generator which creates strong passwords that you can stay safe.") 
username = input("Enter username or Account name:")
###### Getting the length of the password ######
length = int(input("Enter the length of the password you want to creat:"))
punctuationList = "!@#$%&*^/|\?"
characterList = ""
###### Getting character set for password ######
characterList += string.ascii_uppercase
characterList += string.ascii_lowercase
characterList += string.digits
characterList += punctuationList
###### Creating a dictionary for storing passwords ######
passFile = open("passwords.txt","a")
###### Making password ######
password = []
for i in range(length):
    randChar = random.choice(characterList)
    password.append(randChar)
###### Getting the password ######
print("The Generated Password is " + "".join(password))
passFile.write(f"{username} password is "+ "".join(password)+".\n")

