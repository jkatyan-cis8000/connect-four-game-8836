# Connect Four Game Architecture

## Overview
A two-player Connect Four game on a 7-column, 6-row grid. Players alternate dropping discs to form four-in-a-row horizontally, vertically, or diagonally.

## Modules

### 1. board.py
**Responsibility**: Manages the game state grid, disc placement, and win detection.

**Interfaces**:
- `create_board() -> list[list[str]]`: Returns a 6x7 empty grid
- `drop_piece(board, col, player) -> tuple[bool, int]`: Attempts to drop a disc; returns (success, row_index)
- `check_win(board, row, col, player) -> bool`: Checks if the last move created a winning line
- `is_full(board) -> bool`: Checks if the board has no empty spaces
- `print_board(board)`: Displays the board state to console

**File**: `connect_four/board.py`

---

### 2. player.py
**Responsibility**: Handles player input and move validation.

**Interfaces**:
- `get_player_move(board, player) -> int`: Prompts player for a column, validates input
- `validate_move(board, col) -> bool`: Checks if column is valid and not full
- `get_column_input(prompt) -> str`: Gets raw input from player

**File**: `connect_four/player.py`

---

### 3. game.py
**Responsibility**: Orchestrates the game flow and manages player turns.

**Interfaces**:
- `switch_player(current_player) -> str`: Returns the next player
- `play_game()`: Main game loop - alternates turns until win or draw
- `declare_winner(player)`: Announces the winning player
- `declare_draw()`: Announces a draw game

**File**: `connect_four/game.py`

---

### 4. main.py
**Responsibility**: Entry point that initializes and starts the game.

**Interfaces**:
- `main()`: Entry point function

**File**: `main.py`

---

## Game Flow
1. Initialize empty 6x7 board
2. Player 1 (X) chooses a column
3. Disc drops to lowest available row in that column
4. Check for win (4-in-a-row) or draw (full board)
5. If no win/draw, Player 2 (O) takes turn
6. Repeat until game ends

## Win Detection
Check 4 directions from last move:
- Horizontal: left-right
- Vertical: up-down
- Diagonal: up-left to down-right
- Anti-diagonal: up-right to down-left
