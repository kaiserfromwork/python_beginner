
print("Welcome to Guess the number!\n")
number = input("Please, enter a number between 0 and 100 for me to guess.")
print("Let the games begin!\n")

# could use upper and bottom variables to change range if wanted
upper = 100
bottom = 0
guess = (upper + bottom) // 2
counter = 0

while True:
    counter += 1
    answer = input(f"Your number is {guess}! (y/h/l)\n").lower()
    if answer.lower() == "y":
        print("Thank you for playing!")
        print(f'Attempts: {counter}')
        break
    else:
        if answer == "h":
            bottom = guess
            guess = ((upper - guess) // 2) + guess
        else:
            upper = guess
            guess = guess - ((guess - bottom)//2)
