# Try it yourself 7-4 - Page 160

prompt = "\nPlease enter a topping you would like to add to your pizza:"
prompt += "\n(If you're done with your toppings, please type 'quit'.) "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message + " has been added to your pizza!")

# 7-5

prompt = "\nPlease input your age to find out how much your ticket will cost:"
prompt += "\n(Please type 'quit' once you are done.) "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False

    elif int(message) < 3:
        print("Your ticket is free.")
    elif int(message) <= 12:
        print("Your ticket costs $10.00")
    else:
        print("Your ticket costs $15.00")

