import chess
import chess.engine
import os

# Path to Stockfish executable (update this path with your Stockfish binary location)
STOCKFISH_PATH = "stockfish/stockfish-ubuntu-x86-64-sse41-popcnt"

def play_stockfish():
    print("Welcome to Chess against Stockfish!")
    print("Type 'quit' to exit the game.")

    # Initialize the board and Stockfish engine
    board = chess.Board()
    try:
        with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:
            while not board.is_game_over():
                print("\n" + str(board))
                if board.turn == chess.WHITE:
                    # User's turn
                    move = input("Your move (e.g., e2e4): ").strip()
                    if move.lower() == "quit":
                        print("Game exited.")
                        return
                    try:
                        board.push_uci(move)
                    except ValueError:
                        print("Invalid move. Please try again.")
                        continue
                else:
                    # Stockfish's turn
                    print("Stockfish is thinking...")
                    result = engine.play(board, chess.engine.Limit(time=2.0))
                    board.push(result.move)
                    print(f"Stockfish played: {result.move}")

            # Game over
            print("\n" + str(board))
            print("\nGame Over!")
            print("Result:", "1-0" if board.result() == "1-0" else "0-1" if board.result() == "0-1" else "1/2-1/2")
            print(board.result())
    except FileNotFoundError:
        print("Error: Stockfish executable not found. Please update the STOCKFISH_PATH variable.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    play_stockfish()
