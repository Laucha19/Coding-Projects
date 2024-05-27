def build_person(first_name, last_name):
    """Return a dicitonary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('james', 'hetfield')
print(musician)

def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('kirk', 'hammet', 'age=57')
print(musician)
