from connect_four.board import create_board, drop_piece, check_win, is_full, print_board
from connect_four.player import get_player_move


def switch_player(current_player: str) -> str:
    """Returns 'O' if current is 'X', else 'X'."""
    return 'O' if current_player == 'X' else 'X'


def declare_winner(player: str) -> None:
    """Prints winning message."""
    print(f"Player {player} wins!")


def declare_draw() -> None:
    """Prints draw message."""
    print("It's a draw!")


def play_game() -> None:
    """Main game loop that runs until win or draw."""
    board = create_board()
    current_player = 'X'
    
    while True:
        print_board(board)
        
        col = get_player_move(board, current_player)
        success, row = drop_piece(board, col, current_player)
        
        if check_win(board, row, col, current_player):
            print_board(board)
            declare_winner(current_player)
            break
        
        if is_full(board):
            print_board(board)
            declare_draw()
            break
        
        current_player = switch_player(current_player)
