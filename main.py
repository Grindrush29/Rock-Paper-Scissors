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

import random
user1 = int(input("What do you choose? Type 0 for rock, 1 for scissors or 2 for papper\n"))

# Computer randomly chooses sign
computer_sign = ["r", "s" , "p"]
index = int(random.randint(0, 2))
comp = index                   


#Win conditions
if user1 == 0 and comp == 1:
  print(rock)

  print("Computer choose:")

  print(scissors)

  print("You Win")

if user1 == 1 and comp == 2:
  print(scissors)

  print("Computer choose:")

  print(paper)

  print("You Win")

if user1 == 2 and comp == 0:
  print(paper)

  print("Computer choose:")

  print(rock)

  print("You Win")



# Tie conditions
elif user1 == 0 and comp == 0:
  print(rock)

  print("Computer choose:")

  print(rock)

  print("It's a tie")


elif user1 == 1 and comp == 1:
  print(scissors)

  print("Computer choose:")

  print(scissors)

  print("It's a tie")


elif user1 == 2 and comp == 2:
  print(paper)

  print("Computer choose:")

  print(paper)

  print("It's a tie")


  
  
# You lose conditions
elif user1 == 0 and comp == 2:
  print(rock)

  print("Computer choose:")

  print(paper)

  print("You lose")


  
elif user1 == 1 and comp == 0:
  print(scissors)

  print("Computer choose:")

  print(rock)

  print("You lose")


  
elif user1 == 2 and comp == 1:
  print(paper)

  print("Computer choose:")

  print(scissors)

  print("You lose")

























