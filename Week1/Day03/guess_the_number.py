import random
mySecretNumber = random.randint(1, 100)
print("I am thinking of a number between 1 and 100.")

# Player is allowed to guess 6 times
for guessTaken in range(1, 7):
    guess = int(input("Take a guess:"))
    if guess < mySecretNumber:
        print(f"Guess a higher number than {guess}")
    elif guess > mySecretNumber:
        print(f"Guess a lower number than {guess}")
    else:
        break   # Guess was correct, exit the guessing loop.

if guess == mySecretNumber:
    print(f"Excellent! It took you {guessTaken} guesses to guess the right number")
else:
    print(f"The number I choose was {mySecretNumber}")