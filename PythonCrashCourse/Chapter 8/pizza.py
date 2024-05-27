def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping.title())

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Adding multiple arguments to function with arbitrary parameter

def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping.title())

make_pizza(16, 'mushrooms')
make_pizza(25, 'pepperoni', 'green peppers', 'sausage', 'olives')