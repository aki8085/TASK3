import random

secret = random.randint(1, 50)
attempts = 0

print("Guess the secret number between 1 and 50!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low! Try higher.")
    elif guess > secret:
        print("Too high! Try lower.")
    else:
        print(f"Correct! You guessed it in {attempts} attempt(s).")
        break