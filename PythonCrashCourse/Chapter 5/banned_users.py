banned_users = ['andrew', 'carolina', 'david']
user = ['marie', 'carlos']

if user not in banned_users:
    print(user[0].title() + ", you can post a response if you wish.")


car = 'toyota'

print(car == 'toyota')
print(car == 'honda')
print(car.lower() == 'toyota')

age = 18
age_1 = 21

print("\n")
print(age == 18)
print(age != 17)
print(age > 17)
print(age < 21)
print(age >= 5)
print(age <= 99)
print('\n')
print(age == 18 and age > 19)
print(age == 18 and age > 17)
print(age == 18 or age > 17)

print('carolina' in banned_users)
print('marie' in banned_users)

if user not in banned_users:
    print(user[1].title() + ', congratulations. You are not banned from Nintendo Switch online. HA JK, '
                            'get that ass banned SPOOK.')

