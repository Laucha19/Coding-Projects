message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + '!')

prompt = "\nIf you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
prompt += "\nWait... before you tell us, what is your middle name? "

name = input(prompt)
print("\nHello, " + name + '!')