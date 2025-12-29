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
user=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
comp=random.randint(0,2)
if user==0 :
    print(rock)
    print("Computer chose:")
    if comp==0:
        print(rock)
        print("It's a draw")
    elif comp==1:
        print(paper)
        print("You lose")
    else:
        print(scissors)
        print("You win!")
elif user==1:
    print(paper)
    print("Computer chose:")
    if comp == 0:
        print(rock)
        print("You Win!")
    elif comp == 1:
        print(paper)
        print("It's a draw")
    else:
        print(scissors)
        print("You lose")
else :
    print(scissors)
    print("Computer chose:")
    if comp == 0:
        print(rock)
        print("You lose")
    elif comp == 1:
        print(paper)
        print("You Win!")
    else:
        print(scissors)
        print("It's a draw")

