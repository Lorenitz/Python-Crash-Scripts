#List Slices

players=['charles', 'martina', 'michel', 'florence', 'eli']
print(players[0:3])
print(players[1:4]) # It starts on position 1 (Martina), and goes until position 4 (Florence)
print(players[:4])  # Without a starting index, Python starts at the beginning of the list
print(players[-3:]) # Printing the last three players


#Looping Through a Slice

print("Here are the first three players on my team:")

for player in players[:3]:
    print(player.title())

