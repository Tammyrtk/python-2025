players = {
    'flash': 'Dwayne Wade',
    'king james': 'Lebron James',
    'klaw': 'Kahwi Leonard',
    'Melo': 'Carmelo Anthony',
    'chef': 'Stephen Curry',
    'black jesus': 'Micheal Jordan',
    'dame time': 'Damian Lillard',
}

players['klay'] = 'klay Thompsom'

# UPGrade the melo
# players['Melo']= 'Lamelo Ball'

# del players['dame time']
result = players.pop("ky", 'Kyrie Irving')
print(result)
mvp = players.pop('Melo')
print(mvp)

print()

# for key in players:
#    print(key, players[key], sep=", ")
for key, value in players.items():
    print(key, value, sep=", ")
