# Try it yourself 6-4, 6-6 - Page 141

programming_terms = {
    'string': 'A set of words or numbers printed into a block of code.',
    'list': 'A series of objects or numbers wrapped in brackets under one variable name.',
    'for loop': 'A function used for Python to autmatically loop through entire lists.',
    'methods': 'In-built functions to help you display data in a certain way.',
    'if statement': 'A way to check if a value is true or not within a function or program.',
    }

for term, definition in programming_terms.items():
    print("\nTerm: " + term.title())
    print("Definition: " + definition)

# 6-5

rivers = {
    'nile': 'egypt',
    'dark': 'castlevania',
    'bloody': 'norway',
    }

for river, country in rivers.items():
    print("\nThe " + river.title() + " river is located in " + country.title() + ".")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

# 6-6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['jen', 'sarah']
for name in favorite_languages:
    if name in friends:
        print(name.title() + ", Thank you for participating beautiful <3.")
    else:
        print(name.title() + " kys.")

if 'lautaro' not in favorite_languages:
    print("Lautaro, please consider taking our poll!")
