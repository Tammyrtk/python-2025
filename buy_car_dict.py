available_cars = {"1": "toyota",
                  "2": "honda",
                  "3": "ford",
                  "4": "acura",
                  "5": "tesla",
                  }

current_choice = None
cars = {}

while current_choice != "0":
    if current_choice in available_cars:
        chosen_car = available_cars[current_choice]
        if current_choice in cars:
            print(f"Removing {chosen_car}")
            cars.pop(current_choice)
        else:
            print(f"adding {chosen_car}")
            cars[current_choice] = chosen_car
        print(f"you now have : {cars}")
    else:
        print("please print options from the list")
        for key, value in available_cars.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")
    