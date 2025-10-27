import random

n = random.randint(1, 20)
tries = 0
max_tries = 7

print("Welcome to the Number Guessing Game!")
print("You have 7 attempts to guess the number between 1 and 20.\n")
print("If you correctly guess in 2 attempts you get 10 points for each attemp.")
print("If you correctly guess in 4 attempts you get 8 points for each attemp.")
print("If you correctly guess in above 4 attempts you get 6 points for each attemp.\n")

while True:
    guess = int(input("Guess the number: "))
    tries += 1

    if guess == n:
        if tries <= 2:
            score = tries * 10
        elif tries <= 4:
            score = tries * 8
        else:
            score = tries * 6
        print(f"Correct! You guessed in {tries} tries. Your score: {score}")
        break

    elif guess > n:
        print("Wrong guess — try a lower number.")
    else:
        print("Wrong guess — try a higher number.")

    if tries == max_tries:
        print(f"You've used all {max_tries} attempts! The number was {n}.")
        break
