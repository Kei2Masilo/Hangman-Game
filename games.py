import random


# Define ANSI color codes
RESET = "\033[0m"          # Reset to default
BLACK_BG = "\033[40m"      # Black background
YELLOW = "\033[33m"        # Mustard yellow text

def tic_tac_toe():
    def print_board(board):
        print("\n")
        for row in board:
            print(YELLOW + BLACK_BG + " | ".join(row) + RESET)
            print(YELLOW + BLACK_BG + "-" * 5 + RESET)
        print("\n")
    
    def check_winner(board, mark):
        # Check rows, columns, and diagonals
        return (
            any(all(cell == mark for cell in row) for row in board) or
            any(all(row[i] == mark for row in board) for i in range(3)) or
            all(board[i][i] == mark for i in range(3)) or
            all(board[i][2 - i] == mark for i in range(3))
        )
    
    def get_available_moves(board):
        return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    
    print(YELLOW + BLACK_BG + "Welcome to Tic-Tac-Toe!" + RESET)
    board = [[" " for _ in range(3)] for _ in range(3)]
    user_mark = YELLOW + "X" + RESET
    computer_mark = YELLOW + "O" + RESET
    
    print_board(board)
    
    for turn in range(9):
        if turn % 2 == 0:  # User's turn
            while True:
                try:
                    move = input(YELLOW + "Enter your move (row and column 1-3, e.g., 1 2): " + RESET)
                    row, col = map(int, move.split())
                    row, col = row - 1, col - 1
                    if board[row][col] == " ":
                        board[row][col] = user_mark
                        break
                    else:
                        print(YELLOW + "Invalid move. Cell is already taken." + RESET)
                except (ValueError, IndexError):
                    print(YELLOW + "Invalid input. Please enter row and column as two numbers between 1 and 3." + RESET)
        else:  # Computer's turn
            row, col = random.choice(get_available_moves(board))
            board[row][col] = computer_mark
            print(YELLOW + f"Computer chose: {row + 1} {col + 1}" + RESET)
        
        print_board(board)
        
        if turn >= 4:  # Minimum moves required to win
            if check_winner(board, user_mark):
                print(YELLOW + "Congratulations, you win!" + RESET)
                return
            elif check_winner(board, computer_mark):
                print(YELLOW + "Computer wins! Better luck next time." + RESET)
                return
    
    print(YELLOW + "It's a draw!" + RESET)

def hangman():
    words = ["python", "hangman", "random", "computer", "programming"]
    word = random.choice(words)
    guessed = set()
    attempts = 6
    
    print(YELLOW + BLACK_BG + "Welcome to Hangman!" + RESET)
    print(YELLOW + "_ " * len(word) + RESET)
    
    while attempts > 0:
        guess = input(YELLOW + "Guess a letter: " + RESET).lower()
        if not guess.isalpha() or len(guess) != 1:
            print(YELLOW + "Invalid input. Please guess a single letter." + RESET)
            continue
        
        if guess in guessed:
            print(YELLOW + "You already guessed that letter!" + RESET)
            continue
        
        guessed.add(guess)
        if guess in word:
            print(YELLOW + "Correct!" + RESET)
        else:
            print(YELLOW + "Wrong!" + RESET)
            attempts -= 1
        
        current_word = "".join(letter if letter in guessed else "_" for letter in word)
        print(YELLOW + " ".join(current_word) + RESET)
        
        if "_" not in current_word:
            print(YELLOW + f"Congratulations, you guessed the word: {word}!" + RESET)
            return
        
        print(YELLOW + f"Attempts left: {attempts}" + RESET)
    
    print(YELLOW + f"Game over! The word was: {word}" + RESET)

def main():
    print(YELLOW + BLACK_BG + "Choose a game to play:" + RESET)
    print(YELLOW + "1. Tic-Tac-Toe" + RESET)
    print(YELLOW + "2. Hangman" + RESET)
    choice = input(YELLOW + "Enter your choice (1 or 2): " + RESET)
    
    if choice == "1":
        tic_tac_toe()
    elif choice == "2":
        hangman()
    else:
        print(YELLOW + "Invalid choice. Exiting." + RESET)

if _name_ == "_main_":
    main()