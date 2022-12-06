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
import random

game = [rock, paper, scissors]
user_choise = int(input('What do you choose? 0 for rock, 1 for paper, 2 for scissors? \n'))
if user_choise > 2 or user_choise < 0:
  print("You lose because you didn't stick to the rule.")
else:
  print(game[user_choise])
  computer_choise = random.randint(0, 2)
  print("Computer chose:\n" + game[computer_choise])


  if computer_choise - user_choise == 1 or computer_choise - user_choise == -2:
    print("You lose.")
  elif computer_choise - user_choise == -1 or computer_choise - user_choise == 2:
    print("You win!")
  elif computer_choise - user_choise == 0:
    print("It's a draw")
