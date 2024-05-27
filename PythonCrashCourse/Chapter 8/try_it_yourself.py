# Try it yourself 8-6 - Page 179

def city_country(city, country):
    full_location = city + ", " + country
    return full_location.title()

home_town = city_country('miami', 'united states')
print(home_town)

home_town = city_country('buenos aires', 'argentina')
print(home_town)

home_town = city_country('lima', 'peru')
print(home_town)

# 8-7

def make_album(artist_name, album_title, tracks=""):
    album = {'artist': artist_name, 'album': album_title}
    if tracks:
        album['tracks'] = tracks
    return album

record = make_album('megadeth', 'rust in peace', 11)
print(record)

record = make_album('metallica', 'ride the lightning', 12)
print(record)

record = make_album('megadeth', "peace sells... but who's buying?", 13)
print(record)

# 8-8

def make_album(artist_name, album_title):
    album = {'artist': artist_name, 'album': album_title}
    return album

while True:
    print("\nWhat is your favorite artist's name?")
    print("If you want to quit, please type 'quit'.")

    a_name = input("Artist name: ")
    if a_name == 'quit':
        break
    a_title = input("Favorite Album: ")
    if a_title == 'quit':
        break

    record = make_album(a_name, a_title)
    print("\nYour favorite artist is " + a_name.title() + " and your favorite album is " + a_title.title() + ".")

