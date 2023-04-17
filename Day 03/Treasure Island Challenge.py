print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
path = input("Choose a path, left or right? ").lower()

if path == "right":
    print("You were bitten by a snake. Game over!")
elif path == "left":
    lake_path = input("You arrived on a lake. You want to swim or wait? \n").lower()
    if lake_path == "swim":
        print("You were eaten by a crocodile. Game over!")
    elif lake_path == "wait":
        print("A friend arrived and left you on cross path with three doors.")
        cross_path = input("You'll choose the red, blue or yellow one? \n").lower()
        if cross_path == "red":
            print("You were burned by fire. Game over!")
        elif cross_path == "blue":
            print("You were eaten by beasts. Game over!")
        elif cross_path == "yellow":
            print("You find the treasure. You won!")
        else:
            print("Game over!")
