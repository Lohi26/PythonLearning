# Make a rock, paper, scissors game.

# Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

# Start the game by asking the player:

# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

# From there you will need to figure out:

# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.

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

#Write your code below this line 👇

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
arr=["rock","paper","scissors"]
user=int(input())
rand=random.randint(0,2)
print("Your choice:\n")
if user==0:
    print("Rock\n"+rock)
elif user==1:
    print("Paper\n"+paper)
elif user==2:
    print("Scissors\n"+scissors)

print("Computer's choice:\n")
if rand==0:
    print("Rock\n"+rock)
elif rand==1:
    print("Paper\n"+paper)
elif rand==2:
    print("Scissors\n"+scissors)

if user==rand:
    print("Draw!")
elif user==0 and rand==2:
    print("You Win1")
elif user==2 and rand==0:
    print("Computer wins the game!")
elif user==2 and rand==1:
    print("You Win!")
elif user==1 and rand==2:
    print("Computer wins the game!")
elif user==1 and rand==0:
    print("You Win!")
elif user==0 and rand==1:
    print("Computer wins the game!")
else:
    print("Ypu typed an invalid number")
