def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, cols, diagonals
    for row in board:
        if all(c == player for c in row): return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)): return True
    if all(board[i][i] == player for i in range(3)): return True
    if all(board[i][2-i] == player for i in range(3)): return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        try:
            move = input(f"Player {current_player}, enter row and col (0-2) separated by space: ")
            r, c = map(int, move.split())
            
            if board[r][c] != " ":
                print("Cell already taken. Try again.")
                continue
                
            board[r][c] = current_player
            print_board(board)
            
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
                
            if is_full(board):
                print("It's a draw!")
                break
                
            current_player = "O" if current_player == "X" else "X"
            
        except (ValueError, IndexError):
            print("Invalid input. Please enter two numbers between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()
