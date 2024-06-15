import random as rd
import string
length=input("Please enter the desired Password length: ")
while not length.isnumeric():
    length=input("Please enter valid length: ")
complexity=input("""Please enter complexity of the Password:
                 1 for Strong
                 2 for Moderate
                 3 for Easy:
                 """)
if complexity=="1":
    Character = string.ascii_letters + string.digits + string.punctuation
elif complexity=="2":
    Character = string.ascii_letters + string.digits
else:
    Character = string.ascii_letters
Password=''.join(rd.choices(Character,k=int(length)))
print("Your Password is:",end=" ")
print(Password)