numbers = {*""}

print(numbers, type(numbers))

# numbers.add(2)
# print(numbers)

# while len(numbers) < 4:     # 4 unique values not itterating up to 4
#     next_value = int(input('please enter next value'))
#     numbers.add(next_value)
# print(numbers)

data = ['blue', 'red', 'green', 'orange', 'red', 'white', 'blue']

# remove duplicates
# unique_data = set(data)
unique_data = sorted(set(data))
print(unique_data)

# create A list of colors, keeping the order they appear    |   in order
unique_data = list(dict.fromkeys(data))
print(unique_data)

print()
print(dict.fromkeys(data))
