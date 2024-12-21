from simple_deepcopy import my_deepcopy
import copy

original = {
    "Tim": ["Duncan", ["San Antonio Spurs", "PF"]],
    "Kobe": ["Bryant", ["Los Angeles Lakers", "SG"]],
}

copy1 = copy.deepcopy(original)
copy2 = my_deepcopy(original)

original["Kobe"].append("Mamba")
original["Tim"].append("Timmy")

original["Tim"][1].append("Post")
kobe_list = original["Kobe"]
kobe_list[1].append("24")


original
print(original)
print(copy1)
print(copy2)
