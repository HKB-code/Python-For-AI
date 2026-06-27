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
game = [rock,paper,scissors]

while True:
    user_input = int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors. \n"))
    if user_input>=3:
     print("Invalid number")
    else:
        print(game[user_input])
        computer_choice = random.randint(0,2)
        print(game[computer_choice])
        if computer_choice ==0 and user_input ==2 :
            print("You Loose")
        elif computer_choice ==2 and user_input ==0:
            print("You win")
        elif computer_choice>user_input:
            print("you loose")
        elif user_input>computer_choice:
            print("you win")
        else:
            print("draw")
