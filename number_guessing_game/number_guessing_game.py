import random
number = random.randint(1,100)
guess = None

print("Guess the number between one and hundred: ")
while(guess!=number):
    guess = int(input("Enter your guess: "))

    if(guess<number):
        print("Too Low")
    elif(guess>number):
        print("Too high")
    else:
        print("Correct you guessed it")