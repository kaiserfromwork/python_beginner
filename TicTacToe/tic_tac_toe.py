def display_board(board: list) -> None:
    """
    Returns a board format output of the 2d list
    :param board: board to be printed
    :return: prints 2d list to simulate a board
    """
    print("-" * 10)
    for row in board:
        print(" | ".join(str(cell) if cell != "" else " " for cell in row))
    print("-" * 10)


def create_board(size: int = 3) -> list:
    """
    Creates a board using params passed
    :param size: size of the board to be created
    :return: returns a 2d list
    """
    new_board = [[(j * 3 + x + 1) for x in range(size)] for j in range(size)]
    return new_board


def make_move(player: str, move: tuple, board: list) -> bool:
    """
    Returns true if player move is valid!
    :param player: String representing player making the move.
    :param move: Coordinates/Index of the move.
    :param board: Game board (2d list)
    :return: boolean value that determines if move is valid.
    """
    if not (move and player and board):
        return False
    else:
        if board[move[0]][move[1]] not in ["X", "O"]:
            board[move[0]][move[1]] = "X" if player == "P1" else "O"

    return True


def check_for_winner(player: str, board: list) -> bool:
    """
    Checks for a player that completed the game.
    :param player: string representing player that made the move
    :param board: game board (2d list)
    :return: Returns true if there's a player that completed a Column, Diagonal or Row
    """
    check_diagonal = []
    check_reverse_diagonal = []
    move_icon = ""

    if player == "P1":
        move_icon = "X"
    if player == "P2":
        move_icon = "O"

    # checking rows for winner and returns TRUE. moves to columns if not found
    for x in range(len(board)):
        check_column = []
        if all(_ == move_icon for _ in board[x]):
            return True

        # checking columns, adds the value of each column to a list and checks it is a match and returns TRUE
        # if not, it moves on to the next column.
        for j in range(len(board)):
            check_column.append(board[j][x])

            # checks diagonal and return True if it is a match
            if x == j:
                check_diagonal.append(board[x][j])

            # checks reverse diagonal and returns True if it is a match
            if x + j == (len(board) - 1):
                check_reverse_diagonal.append(board[x][j])

        # Checking if column is completed
        if all(_ == move_icon for _ in check_column):
            return True

    # Diagonal and Reverse Diagonal are checked once after the looping it done.
    if len(check_reverse_diagonal) == len(board) and all(_ == move_icon for _ in check_reverse_diagonal):
        return True

    if len(check_diagonal) == len(board) and all(_ == move_icon for _ in check_diagonal):
        return True

    return False


if __name__ == "__main__":
    board = create_board(3)
    valid_coordinates = {
        0: (0, 0), 1: (0, 1), 2: (0, 2),
        3: (1, 0), 4: (1, 1), 5: (1, 2),
        6: (2, 0), 7: (2, 1), 8: (2, 2),
    }
    winner = ""
    current_player = "P1"
    player = None

    print("Welcome to TIC TAC TOE GAME!")

    # Game logic. each while loop is a player turn. player turn changes once current player made a valid move.
    # While loop ends if no more valid moves available.
    while len(valid_coordinates) > 0:
        if current_player == "P1":
            move = "X"
        else:
            move = "O"

        display_board(board)

        # try block to prevent user from entering and invalid (none integer) value.
        try:
            player = int(
                input(f"You're '{move}'!\nWhere would like to play? (Pick one of the numbers being displayed)\n")) - 1
        except ValueError:
            print("Invalid input! Please pick one of the numbers being displayed!")
            display_board(board)
            continue # Restart the loop since player will be None unless input is valid

        if player >= 0 and player in valid_coordinates:
            if make_move(current_player, valid_coordinates[player], board):
                del valid_coordinates[player]
                if check_for_winner(current_player, board):
                    winner = current_player
                    break
                else:
                    current_player = "P2" if current_player == "P1" else "P1"
            else:
                print("Invalid input!")
                continue
        else:
            print("Invalid Input!")
            continue

    if len(valid_coordinates) == 0 and winner:
        print(f'Winner of the game is {winner}')
    else:
        print("Game ends in a Draw!")
