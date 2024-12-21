# 201   203
d = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    "iv": "four",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

v = d.values()
print(v)

d[10] = 'ten'
print(v)

print('four' in v)
print('eleven' in v)

keys = list(d.keys())
values = list(v)
if 'four' in values:
    index = values.index('four')
    key = keys[index]
    print(f'{d[key]} was found with the key {key}')

print()

for key, value in d.items():
    if value == "five":
        print(f'{d[key]} was found with the key {key}')

# 2222222222222222222222222222222222222222222222222

# d2 = {
#     7: 'KD',
#     23: 'lebron',
#     0: 'westbrook',
# }
#
# d.update(d2)
# for key, value in d.items():
#     print(key, value)
#
# print()
#
# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)


# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)
# -------------------------------------
# ------------

# keys = d.keys()
# print(keys)
#
# for item in d:
#     print(item)
#