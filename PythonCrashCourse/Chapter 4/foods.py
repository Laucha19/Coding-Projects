my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('canoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Try it yourself 4-10 - Page 102

characters = ['lucina', 'mario', 'joker', 'wario', 'cpt falcon']
print("The first three characters of the list are:")
print(characters[0:3])

print("\nThe three characters in the middle of the list are:")
print(characters[1:4])

print("\nThe last three characters on the list are:")
print(characters[2:5])

# 4-11

pizzas = ['pepperoni', 'tomatoe', 'onion']
friend_pizza = pizzas[:]

pizzas.append('sausage')
friend_pizza.append('mushroom')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for friends in friend_pizza:
    print(friends)

# 4-12

foods = ['pasta', 'hamburgers', 'salad', 'fish n chips']
competitor_foods = ['tacos', 'burritos', 'chalupas', 'tamales']

print("\nThis is a list of my own restaurant's food menu, please enjoy:")
for food in foods:
    print(food.title())

print("\nThis is a list of my competitors menu, build the wall, BUILD THE WALL!!!:")
for competitor in competitor_foods:
    print(competitor.title())