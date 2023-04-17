print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
combined_names = name1 + name2

count_true = 0
if combined_names.count("t"):
    count_true += combined_names.count("t")
if combined_names.count("r"):
    count_true += combined_names.count("r")
if combined_names.count("u"):
    count_true += combined_names.count("u")
if combined_names.count("e"):
    count_true += combined_names.count("e")

count_love = 0
if combined_names.count("l"):
    count_love += combined_names.count("l")
if combined_names.count("o"):
    count_love += combined_names.count("o")
if combined_names.count("v"):
    count_love += combined_names.count("v")
if combined_names.count("e"):
    count_love += combined_names.count("e")

true_love = int(str(count_true) + str(count_love))

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos")
elif 40 <= true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}")
