age = 17

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

amusement_age = 66

if amusement_age < 4:
    price = 0
elif amusement_age < 18:
    price = 5
elif amusement_age > 65:
    price = 5
else:
    price = 10

print("\nYour admission fee is $" + str(price) + ".")

