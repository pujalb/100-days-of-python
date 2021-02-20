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
user = -1
while (user < 0 or user > 2):
    user = int(input("""What do you choose? Type\
     \n0 for Rock \n1 for Paper \n2 for Scissors\n"""))

choices =[rock, paper, scissors]
print(f"User chose: {user} \n{choices[user]}")

computer = random.randint(0,2)
print(f"Computer chose: {computer} \n{choices[computer]}")

# If both choose the same
if user == computer:
    print("It's a draw.")

# User selects Rock
if user == 0:
    if computer == 1:   # Paper
        print("Paper beats Rock \nYou lose!")
    elif computer == 2: # Scissors
        print("Rock beats Scissors \nYou win!")

# User selects Paper
if user == 1:
    if computer == 2:   # Scissors
        print("Scissors beats Paper \nYou lose!")
    elif computer == 0: # Rock
        print("Paper beats Rock \nYou win!")

# User selects scissors
if user == 2:
    if computer == 0:   # Rock
        print("Rock beats Scissors \nYou lose!")
    elif computer == 1: # Paper
        print("Scissors beats Paper \nYou win!")
    

