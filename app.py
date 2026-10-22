import time
import random

def print_board(board):
    print("\n---------")
    for row in board:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
        print("---------")

def play_tic_tac_toe():
    print("=== TIC-TAC-TOE GAME SIMULATION ===")
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    
    moves = [(0,0, "X"), (1,1, "O"), (0,1, "X"), (2,2, "O"), (0,2, "X")]
    
    print_board(board)
    
    for r, c, player in moves:
        time.sleep(1.5)
        board[r][c] = player
        print(f"Player {player} plays at position ({r}, {c})")
        print_board(board)
        
    print("🎉 Game Over: Player X wins the match!\n")

if __name__ == "__main__":
    while True:
        play_tic_tac_toe()
        print("Waiting 15 seconds before starting the next game match...")
        time.sleep(15)