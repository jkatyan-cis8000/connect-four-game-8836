def create_board() -> list[list[str]]:
    """Create a 6x7 empty Connect Four board."""
    return [[' ' for _ in range(7)] for _ in range(6)]


def drop_piece(board: list[list[str]], col: int, player: str) -> tuple[bool, int]:
    """Drop a piece into the specified column.
    
    Returns (success, row_index) where row_index is where the piece landed, or -1 if failed.
    """
    if col < 0 or col >= 7:
        return (False, -1)
    
    for row in range(5, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return (True, row)
    
    return (False, -1)


def check_win(board: list[list[str]], row: int, col: int, player: str) -> bool:
    """Check if the last move created a winning line."""
    directions = [
        (0, 1),   # horizontal
        (1, 0),   # vertical
        (1, 1),   # diagonal down-right
        (1, -1),  # diagonal down-left
    ]
    
    for dr, dc in directions:
        count = 1
        
        # Check positive direction
        r, c = row + dr, col + dc
        while 0 <= r < 6 and 0 <= c < 7 and board[r][c] == player:
            count += 1
            r += dr
            c += dc
        
        # Check negative direction
        r, c = row - dr, col - dc
        while 0 <= r < 6 and 0 <= c < 7 and board[r][c] == player:
            count += 1
            r -= dr
            c -= dc
        
        if count >= 4:
            return True
    
    return False


def is_full(board: list[list[str]]) -> bool:
    """Check if the board is full."""
    return all(board[0][col] != ' ' for col in range(7))


def print_board(board: list[list[str]]) -> None:
    """Display the board with column numbers (1-7) at the bottom."""
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
    print('+-+-+-+-+-+-+-+')
    print(' 1 2 3 4 5 6 7 ')
