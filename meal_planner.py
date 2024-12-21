from contents import pantry, recipes        # 200


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """

    :param item:
    :param data:
    :type amount:
    
    """
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount


display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = {}

while True:
    # display menus
    print('Please choose a recipe')
    print('----------------------')
    for key, value in display_dict.items():
        print(f'{key} - {value}')

    choice = input(': ')

    if choice == '0':
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f'you selected {selected_item}')
        print('checking ingredients')
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f'\t{food_item} OK')
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f'\tGet {quantity_to_buy} {food_item}')
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

for things in shopping_list.items():
    print(things)
