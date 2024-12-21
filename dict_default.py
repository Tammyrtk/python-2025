from contents import pantry

chicken_quantity = pantry.setdefault('chicken', 0)
print(f'There are {chicken_quantity} chickens')

beans = pantry.setdefault('beans', 0)    # setdefault adds key to dict
print(f'beans: {beans}')

ketchup = pantry.get('ketchup', 0)
print(f'ketchup: {ketchup}')

z_quantity = pantry.setdefault('zuchini', 'eight')
print(f'zuchini: {z_quantity}')

print()
print('pantry now contains')

for key, value in sorted(pantry.items()):
    print(key, value)
