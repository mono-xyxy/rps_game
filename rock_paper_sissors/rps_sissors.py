import random

choices = ["rock","papers","sissors"]


user = input("Choose rock/paper/scissors: ")
computer = random.choice(choices)

print("Computer:",computer)

if user==computer:
    print("Draw")
elif (user=="rock"and computer == "sissors") or \
     (user == "paper" and computer == "sissors") or\
     (user=="sissors" and computer == "rock"):
    print("You Win!")
else:
    print("You lose")