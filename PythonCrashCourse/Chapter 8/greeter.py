def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')
greet_user('sarah')
greet_user('dickhead')

# Try it yourself 8-1 - Page 168

def display_message():
    print("In this chapter, I am learning about functions and everything inside of it.")

display_message()

# 8-2
def favorite_book(title):
    print("One of my favorite books is " + title.title() + ".")

favorite_book('el marcianito')
