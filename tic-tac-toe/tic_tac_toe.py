def print_line():
    print("+---" * 3 + '+')


def print_row(row=[' ', ' ', ' ']):
    for value in row:
        print(f"| {value} ", end='')
    print("|")


def print_board(board):
    for row in board:
        print_line()
        print_row(row)
    print_line()


board = [[' '] * 3,
         [' '] * 3,
         [' '] * 3
         ]


def is_end(board, turns):
    # diagonals
    if (board[0][2] == board[1][1] == board[2][0] != ' ') or \
            (board[0][0] == board[1][1] == board[2][2] != ' '):
        print(f"Player {board[1][1]} wins.")
        return True

    # rows
    if board[0][0] == board[0][1] == board[0][2] != ' ':
        print(f"Player {board[0][0]} wins.")
        return True
    if board[1][0] == board[1][1] == board[1][2] != ' ':
        print(f"Player {board[1][0]} wins.")
        return True
    if board[2][0] == board[2][1] == board[2][2] != ' ':
        print(f"Player {board[2][0]} wins.")
        return True
    # columns
    if board[0][0] == board[1][0] == board[2][0] != ' ':
        print(f"Player {board[0][0]} wins.")
        return True
    if board[0][1] == board[1][1] == board[2][1] != ' ':
        print(f"Player {board[1][1]} wins.")
        return True
    if board[0][2] == board[1][2] == board[2][2] != ' ':
        print(f"Player {board[2][2]} wins.")
        return True
    if turns == 9:
        print("It's a Draw")
        return True
    return False


def main():
    print_board(board)
    turns = 0
    player = 'x'
    while not is_end(board, turns):
        row = int(input("Enter row position: "))
        col = int(input("Enter col position: "))
        try:
            board[row][col]
        except IndexError:
            print("This position is not valid")
            continue
        turns += 1
        if board[row][col] != ' ':
            print("This position is already taken")
            continue
        board[row][col] = player  # play

        print_board(board)
        # switch to player
        if player == 'x':
            player = 'o'
        else:  # player == 'o'
            player = 'x'
        print(f"Player {player}'s turn")


if __name__ == "__main__":
    main()

