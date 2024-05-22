# This is a list comprehension (entire function built in one line)

squares = [value**2 for value in range(1,11)]
print(squares)

# Exercises 4-3 to 4-9 - Page 97

for numbers in range(1,21):
    print(numbers)

numbers = list(range(1,101))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1,21,2))
print(odd_numbers)

threes = list(range(3,31,3))
print(threes)

cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)

print(cubes)

cubes = [value**3 for value in range(1,11)]
print(cubes)

