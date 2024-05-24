# Try it yourself 7-8 - Page 164

sandwich_orders = ['ham n cheese', 'pastrami', 'meatball','pastrami', 'turkey',
                   'pastrami', 'tuna']
finished_sandwiches = []
print(sandwich_orders)
print("The Deli has ran out of pastrami! Sorry for the inconvenience.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()

    print("Your " + current_sandwiches.title() + " sandwich is being prepared!")
    finished_sandwiches.append(current_sandwiches)

print("\nThe following sandwiches have been made and ready to eat:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# 7-9

sandwich_orders = ['ham n cheese', 'pastrami', 'meatball','pastrami', 'turkey',
                   'pastrami', 'tuna']
print("\n")
print(sandwich_orders)
print("The Deli has ran out of pastrami! Sorry for the inconvenience.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

# 7-10

dream_vacation = {}
flag = True

while flag:
    name = input("\nWhat is your name young one? ")
    vacation = input("And where is it that you want to vacation in? ")

    dream_vacation[name] = vacation

    repeat = input("Would you like to input someone else's dream vacation? " +
                   "(yes/no) ")
    if repeat == 'no':
        flag = False

print("\n--- Poll Results ---")
for name, vacation in dream_vacation.items():
    print(name.title() + "'s dream vacation is to visit " + vacation.title()
          + "!")

