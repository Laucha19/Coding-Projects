motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# These are chapter 3 exercises, please note I did most of these at work, this is only 3-7

guest_list = ['Rocky', 'Nico', 'Mama']
print("\n", guest_list)
guest_list.insert(0,'Thomasito')
guest_list.insert(2, 'Papa')
guest_list.append('Dinito')

print(guest_list)
print(guest_list[0] + ", you are invited to the 2024 dinner palooza, please take a seat.")
print(guest_list[1] + ", you are invited to the 2024 dinner palooza, please take a seat.")
print(guest_list[2] + ", you are invited to the 2024 dinner palooza, please take a seat.")
print(guest_list[3] + ", you are invited to the 2024 dinner palooza, please take a seat.")
print(guest_list[4] + ", you are invited to the 2024 dinner palooza, please take a seat.")
print(guest_list[5] + ", you are invited to the 2024 dinner palooza, please take a seat.")

print("\nSorry for the inconvenience, only two guests can attend this party, we have lost seats.")
print(guest_list)
popped_guests = guest_list.pop(0)
print(popped_guests + " we are sorry, but you have been uninvited from the dinner party, take care.")
print(guest_list)
popped_guests = guest_list.pop(0 + 1)
print(popped_guests + " sorry but you have to go as well, this is an animal only dinner.")
print(guest_list)
popped_guests = guest_list.pop(1)
print(popped_guests + " it's time to go.... invita al negro si queres el si puede jaja.")
print(guest_list)
popped_guests = guest_list.pop(1)
print(popped_guests + " te quiero mucho... y es el dia de las madres! Pero los ferrizos quieren comer!")
print(guest_list)
print(guest_list[0] + " como te extranio loquito.... veni por una cenita mas que te va a encantar.")
print(guest_list[1] + " hoy es tu dia y podes comer lo que quieres sin cagadera!!! Disfruta pipito.")

del guest_list[0]
del guest_list[0]
print(guest_list)




