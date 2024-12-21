available_cars = {"1": "toyota",
                  "2": "honda",
                  "3": "ford",
                  "4": "acura",
                  "5": "tesla",
                  }

current_choice = None
while current_choice != "0":
    if current_choice in available_cars:
        chosen_car = available_cars[current_choice]
        print(f"adding {chosen_car}")
    else:
        print("please print options from the list")
        for key, value in available_cars.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")
