# These are exercises 3-8 to 3-10 - Page 83

locations = ['rome', 'paris', 'rio de janeiro', 'caracas', 'tokyo']
print("This is the original list from the top of the dome:")
print(locations)

print("\nThis is the list but sorted in alphabetical order:")
print(sorted(locations))

print("\nThis is the original list once again, showing it's back to original order:")
print(locations)


print("\nThis is the locations in REVERSE alphabetical order... permanently?")
print(sorted(locations, reverse=True))

print("\nBack to original order....:")
print(locations)

locations.reverse()
print("\nThis is permanently reversed now:")
print(locations)

locations.reverse()
print("\nJust kidding.... permanently switched back to original order:")
print(locations)

locations.sort()
print("\nThis is order stored in Alphabetical order permanently.")
print(locations)

locations.sort(reverse=True)
print("\nThis is stored in reverse Alphabetical order permanently.")
print(locations)

# 3-9

guest_list = ['Rocky', 'Mama', 'Dinito', 'Papa', 'La Gary', 'Thomasito']
print("\n", guest_list)
print(len(guest_list))

# 3-10

smash_characters = ['mario', 'lucina', 'joker', 'wario', 'isabelle', 'cpt falcon']
print(smash_characters)
smash_characters.append('hero')
print(smash_characters)
smash_characters.insert(0, 'DK')
print(smash_characters)

del smash_characters[1]
print(smash_characters)

popped_smash_characters = smash_characters.pop(3)
print(smash_characters)
print(popped_smash_characters)

smash_characters.remove('isabelle')
print(smash_characters)

smash_characters.sort()
print(smash_characters)
smash_characters.sort(reverse=True)
print(smash_characters)

print(len(smash_characters))

# 3-11

streaming_sites = ['netflix', 'hulu', 'peacock', 'amazon video', 'disney plus']
print(streaming_sites[-1])
