# Try it yourself 8-3 - Page 174

def make_shirt(size, shirt_text):
    print("\nThe size of the shirt is: " + size.title())
    print("The text that will go on the shirt will be: " + shirt_text)

make_shirt('medium', 'I like boobs')
make_shirt(size='large', shirt_text='YOLO')

# 8-4

def make_shirt(shirt_text, size='large'):
    print("\nThe size of the shirt is: " + size.title())
    print("The text that will go on the shirt will be: " + shirt_text)

make_shirt('I love Python')
make_shirt('I love Python', size='medium')
make_shirt(size='small', shirt_text='I like turtles')

# 8-5

def describe_city(city, country='USA'):
    print("\n" + city.title() + " is in " + country + ".")

describe_city('miami')
describe_city('chicago')
describe_city('buenos aires', country='Argentina')
