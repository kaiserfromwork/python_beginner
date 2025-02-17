
print("Welcome to Guess the number!\n")
number = input("Please, enter a number between 0 and 100 for me to guess.")
print("Let the games begin!\n")

# could use upper and bottom variables to change range if wanted
upper, bottom = 100, 0
#guess = (upper + bottom) // 2
guess = (bottom + upper) // 2
counter = 0

while True:
    counter += 1
    answer = input(f"Your number is {guess}! (y/h/l)\n").lower()

    if answer.lower() == "y":
        print(f"Thank you for playing! Attempts {counter}")
        break
    elif answer == 'h':
        bottom = guess + 1
        # bottom = guess
        # guess = ((upper - guess) // 2) + guess
    elif answer == 'l':
        upper = guess - 1
        # upper = guess
        # guess = guess - ((guess - bottom)//2)
    else:
        print("Invalid input! Please enter 'y', 'h', or 'l'.")

    guess = (bottom + upper) // 2