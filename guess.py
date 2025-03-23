guess = 0
tries = 0

while guess != 6:
    guess = int(input("Guess the number: "))
    tries += 1
    if guess == 6:
        print("You guessed it!")
        print(f"It took you {tries} tries.")
    else:
        print("Try again!")