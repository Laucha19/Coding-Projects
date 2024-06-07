# Writing to an empty line and adding multiple lines.

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming. SIKE!\n")
    file_object.write("I love creating new games.\n")

# Appending to a File

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# Try it yourself 10-3 - Page 232

name = input("Hello user, what is your name? ")

guestname = 'guest.txt'

with open(guestname, 'w') as g:
    g.write(name.title() + "\n")

print("-----------------")

# 10-4

guestbook = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
run = True
while run:
    name = input("\nHello user, what is your name? ")
    if name == 'quit':
        break
    else:
        with open(guestbook, 'a') as gbook:
            gbook.write(name.title() + "\n")
            print("Hello " + name.title() + ", you've been added to the guest book.")

# 10- 5

filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")





