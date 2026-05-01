import random
num=random.randint(1, 100)
user=0
attempts=0
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
while user!=num:
    user = int(input("Enter your guess: "))
    attempts += 1
    if user>num:
        print("Too high!")
    elif user<num:
        print("Too low!")
print(f"Correct! You found the number in {attempts} attempts.")
