# Try it yourself 7-1 - Page 154

rental_car = input("Welcome to our website! What kind of rental car are you looking for?: ")
print("Let me see if I can find you a " + rental_car.title() + ".")

# 7-2

dinner_group = input("\nGood evening, and how many people are in your group tonight? ")
dinner_group = int(dinner_group)

if dinner_group > 8:
    print("Sorry, that is way too many people, you will have to wait for a table.")
else:
    print("Please right this way, table for " + str(dinner_group) + ".")

# 7-3

number = input("\nEnter a number and I will tell you if it's a multiple of 10 or not: ")
number = int(number)

if number * 10:
    print("This is a multiple of 10.")
else:
    print("This is not a multiple of 10.")
