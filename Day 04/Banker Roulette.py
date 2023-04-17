import random

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
num_items = len(names)

print(f"{names[random.randint(0, num_items-1)]} is going to buy the meal today!")
