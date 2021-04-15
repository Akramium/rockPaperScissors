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

game_images = [rock, paper, scissors]
my_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors'))
computer_choice = random.randint(0, 2)

print(game_images[my_choice])
print('Computer chose: \n')
print(game_images[computer_choice])

to_win = my_choice > computer_choice

if my_choice >= 3 or my_choice < 0:
    print("You typed a invalid number, you lose.")
elif my_choice == computer_choice:
    print("Equal")
elif to_win:
    print("You win")
else:
    print("You lose")
