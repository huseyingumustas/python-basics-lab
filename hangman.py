import random
# Game setup: list of words and selecting a random target word
words=["apple", "banana", "cherry", "melon", "mango"]
word=random.choice(words)

# Initialize the hidden word with underscores and set up tracking variables
display=["_"]*len(word)
attempts=0
letters=[]# Stores guessed letters to prevent duplicate attempts

print("Welcome to Hangman!")
print(f"The word has {len(word)} letters: " + " ".join(display))

# Game loop continues until all underscores are replaced with correct letters
while "_" in display:
    guess=input("Guess a letter: ").lower()

    # Input validation: ensure it's a single alphabetic character
    if len(guess)!=1 or not guess.isalpha():
        print("Please enter a single valid letter!")
        continue

    # Prevent the user from losing attempts on the same letter
    if guess in letters:
        print(f"You already guessed '{guess}'. Try another one.")
        continue

    # Record the valid guess and increment the counter
    letters.append(guess)
    attempts += 1

    # Check if the guessed letter exists in the word and reveal its positions
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                display[i]=guess
        print("Correct!")
    else:
        print("Incorrect!")

    # Update the player on current progress
    print("".join(display))
print(f"Congratulations! You found the word in {attempts} attempts!")

