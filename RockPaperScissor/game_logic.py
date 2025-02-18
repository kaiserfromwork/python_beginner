import random


# compares players moves using a dict and returns the tie players have same input otherwise returns winner
def winner_logic(p1: str, p2: str) -> str:
    winner_conditions = {
        'r': 'scissors',
        'p': 'rock',
        's': 'paper'
    }

    if p1 == p2[0]:
        return "Tie"
    else:
        return "player 1" if winner_conditions[p1] == p2 else "player 2"


rock_paper_scissor = {
    0: "rock",
    1: "paper",
    2: "scissors"
}

print("Welcome to Rock, Paper and Scissors game!")
player_1_counter = 0
ai_player_counter = 0

while True:

    start = input("Are you ready to play? (y/n)\n").lower()

    if start == "y":
        print("Let's start!")
    elif start == 'n':
        print("Thank you for playing!")
        break
    else:
        print("Please enter 'y' for Yes or 'n' for No.")

    player_1 = input("Enter your move. (R for Rock, P for Paper and S for Scissors or E to end the game)\n").lower()
    valid_input = ('r', 'p', 's', 'e')

    if player_1 not in valid_input:
        print("Input not valid. Please enter a valid input. (R for Rock, P for Paper and S for Scissors or E to end "
              "the game)\n")
        continue

    if player_1 == 'e':
        print("GAME OVER!")
        break

    player_2 = rock_paper_scissor.get(random.randint(0, 2))
    print(f'You play: {player_1}')
    print(f'P2 plays: {player_2}')

    result = winner_logic(player_1, player_2)
    if result == "player 1":
        player_1_counter += 1
        print(f'{result} wins!')
    elif result == "player 2":
        ai_player_counter += 1
        print(f'{result} wins!')
    else:
        print("It's a TIE! Win count remains the same")

    print(f'Score: \n\tPlayer 1: {player_1_counter}\n\tPlayer 2: {ai_player_counter}')
