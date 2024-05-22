user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

print("\n")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
    language.title() + ".")

print ("\n")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

# Using the key() method to find out if a particular person did not take the poll.
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# To print the keys of a dictionary in ORDER with the sorted() function.
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Looping through values in a dictionary.

print("\nThe following programming languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Using a set to eliminate repetitive values and only print unique values:
print("\nThe following languages have been mentioned at least once:")
for language in set(favorite_languages.values()):
    print(language.title())




