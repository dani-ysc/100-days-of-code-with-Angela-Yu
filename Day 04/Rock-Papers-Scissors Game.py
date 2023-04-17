import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print("Player chose:")
if player1 == 0:
    print(rock)
elif player1 == 1:
    print(paper)
elif player1 == 2:
    print(scissors)
else:
    print("You typed an invalid number, you lose!")

print("Computer chose:")
computer = random.randint(0, 2)
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)

if player1 == 0 and computer == 2:
    print("You won!")
elif player1 == 1 and computer == 0:
    print("You won!")
elif player1 == 2 and computer == 0:
    print("You won!")
elif player1 == computer:
    print("It's a draw")
else:
    print("You lose!")
