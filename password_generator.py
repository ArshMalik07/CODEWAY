import random

length = int(input("Enter length: (positive numbers)"))
difficulty = input("Difficulty?(Hard/Medium/Easy)")

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "123456789"
special_characters = "@#$!^&*~"

easy = characters#for easy level password
medium = characters + numbers#for medium password
hard = characters + numbers + special_characters#for hard level password
password = ""


if difficulty.lower() == "hard":
        for i in range(length):
            password += random.choice(hard)
        print(password)

elif difficulty.lower() == "medium":
        for i in range(length):
            password += random.choice(medium)
        print(password)

elif difficulty.lower() == "easy":
        for i in range(length):
            password += random.choice(easy)
        print(password)

else:
        print("Please enter a valid difficulty.(Hard/Medium/Easy)")
