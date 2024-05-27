# Positional Arguments:

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('dog', 'rocky')
describe_pet('cat', 'brunito')
describe_pet('brunito', 'cat')

# Keyword Arguments:

def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='dog', pet_name='rocky')
describe_pet(pet_name='rocky', animal_type='dog')

# Default Value:

def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('willie')
describe_pet('brunito', animal_type='cat')
