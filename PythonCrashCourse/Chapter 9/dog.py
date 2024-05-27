# Introducing a basic example of a Class - CHAPTER 9
class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() +  " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()
print("------------------")

# Try it yourself 9-1 - Page 199

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The name of this restaurant is " + self.restaurant_name.title() + ".")
        print(self.restaurant_name.title() + "'s cuisine type is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant is currently open. Please come by and enjoy some delicious food!")

restaurant = Restaurant('the epico diner', 'pasta')
restaurant_1 = Restaurant('chipotle', 'mexican food')
restaurant_2 = Restaurant('cheesecake factory', 'literally anything')

print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\n")

restaurant_1.describe_restaurant()
print("\n")
restaurant_2.describe_restaurant()
print("-------------------")

# 9-3

class User():

    def __init__(self, first_name, last_name, age, nationality, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.profession = profession
        full_name = self.first_name + " " + self.last_name
        self.full_name = full_name

    def describe_user(self):
        print("Name: " + self.full_name.title())
        print("Age: " + str(self.age))
        print("Nationality: " + self.nationality.title())
        print("Profession: " + self.profession.title())

    def greet_user(self):
        print("Hello " + self.full_name.title() + ", thank you for logging in.")




user_0 = User('lautaro', 'toppino', '32', 'argentina', 'coder')
user_1 = User('john', 'levine', '27', 'united states', 'professional fag')
user_2 = User('carlos', 'hakate', '26', 'nicaragua', 'stay at home dad')

user_0.describe_user()
user_0.greet_user()
print("--------------------")

user_1.describe_user()
user_1.greet_user()
print("--------------------")

user_2.describe_user()
user_2.greet_user()