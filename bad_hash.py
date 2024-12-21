# 211   used to swiftly look up values in a table
# Data breaches
data = {
    ('orange', 'a sweet citrus'),
    ('apple', 'good for making cider'),
    ('lemon', 'a sour yellow citrus'),
    ('grape', 'a unique grape'),
}

# print(ord('a'))     # prints
# print(ord('b'))
# print(ord('z'))


def simple_hash(s: str) -> int:
    basic_hash = ord(s[0])
    return basic_hash % 10


def get(k: str) -> str:
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


# for key, value in data:
#     # h = simple_hash(key)
#     h = hash(key)
#     print(key, h)

keys = [''] * 10
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    # h = hash(key)
    print(key, h)
    keys[h] = key
    values[h] = value

print(keys)
print(values)
print()
value = get('lemon')
print(value)
