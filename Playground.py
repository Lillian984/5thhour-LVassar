
import random

print("Hello world")

User_name = input("Enter your name: ")

User_password = input("Create a password: ")

if User_password == "1234567":
    print("Terrible password. Try again.")
elif User_password == "password":
    print("Password is Good!")

User_birth_month = input("Enter your birth month: ")
User_birth_day = input("Enter your birth day: ")
User_birth_year = input("Enter your birth year: ")

if User_birth_year < "1999" or User_birth_year == "1999":
    print("Dang you are sooo old")
elif "2000" < User_birth_year < "2012":
    print("Okaayyy you are an teen")
elif "2013" < User_birth_year < "2026":
     print("Dang you are an infant")

pick_a_number = int(input("Enter a number from this list: "))

random_number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(random_number_list)
print(random_number_list)