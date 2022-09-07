import random
import string

password_array = "" #сюди записую всі елементи
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
numbers = "0123456789"
special_characters = "!?#$%^&*()+@-"

lower_letter = "YES"
if lower_letter == "YES":
    password_array = password_array + lower_letters

while True:
    upper_letter = input("Do you want to add upper case letters to your random password? YES/NO: ").upper()
    if upper_letter == "NO" or upper_letter == "YES":
        break
    else:
        print(upper_letter + " is not valid!", end=" ")

if upper_letter == "YES":
    password_array = password_array + upper_letters

while True:
    number = input("Do you want to add numbers to your random password? YES/NO: ").upper()
    if number == "YES" or number == "NO":
        break
    else:
        print(number + " is not valid!", end=" ")

if number == "YES":
    password_array = password_array + numbers

while True:
    special_character = input("Do you want to add special characters to your random password? YES/NO: ").upper()
    if special_character == "YES" or special_character == "NO":
        break
    else:
        print(special_character + " is not valid!", end=" ")

if special_character == "YES":
    password_array = password_array + special_characters

while True:
    size = int(input("Set of symbols to create password (6-32): "))
    if 6 <= size <= 32:
        break
    else:
        print(str(size) + " is not valid!", end=" ")


password = random.choices(password_array, k = size)
print("".join(password))

