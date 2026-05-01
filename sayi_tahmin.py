import random
num=random.randint(1, 100)
user=int(input("guess the number(1-100): "))
attempts=1
while user!=num:
    if user>num:
        print("Too high!")
        attempts+=1
    elif user<num:
        print("Too low!")
        attempts+=1
    user=int(input("guess again: "))
print(f"Correct! You found the number in {attempts} attempts.")
