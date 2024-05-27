# Try it yourself 8-12 - Page 187

def make_sandwich(*ingredients):
    print("\nHere is what you ordered on your sandwich:")
    for ingredient in ingredients:
        print("- " + ingredient.title())

make_sandwich('ham', 'tomatoes')
make_sandwich('cheese')
make_sandwich('chicken', 'mayo', 'lettuce', 'pickles', 'tomatoes', 'onions')

# 8-13

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('lautaro', 'toppino',
                             age='32',
                             nationality='argentina',
                             hobbies=['gaming', 'guitar', 'exercise'])
print("--------------------------")
print(user_profile)

# 8-14
def build_car_info(manufacturer, model, **car_info):
    car = {}
    car['manufacturer_name'] = manufacturer
    car['model_name'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

make_car = build_car_info('toyota', 'corolla',
                          color='white',
                          size='cedan',
                          interior='black')
print(make_car)

