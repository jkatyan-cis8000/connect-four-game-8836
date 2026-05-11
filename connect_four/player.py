def validate_move(board, col) -> bool:
    """Check if column is valid (0-6) and not full."""
    if col < 0 or col > 6:
        return False
    return board[0][col] == ' '


def get_column_input(prompt) -> str:
    """Get raw input from player."""
    return input(prompt)


def get_player_move(board, player) -> int:
    """Prompt player for a column, validate input, return 0-indexed column."""
    while True:
        prompt = f"Player {player}, choose a column (1-7): "
        user_input = get_column_input(prompt)
        
        try:
            col = int(user_input)
            if col < 1 or col > 7:
                print("Invalid input. Please enter a number between 1 and 7.")
                continue
            
            zero_indexed_col = col - 1
            if not validate_move(board, zero_indexed_col):
                print("Column is full. Please choose another column.")
                continue
            
            return zero_indexed_col
        
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
