# Chess Game Project

## Overview
This project is a Python-based chess game that integrates a visualization layer using Pygame and utilizes the `python-chess` library for game logic and Stockfish as the AI opponent. It aims to provide a modular architecture for easy development and future expansion.

---

## Features
- Interactive chess game playable against the Stockfish engine.
- Modular architecture for easy maintenance and scalability.
- Pygame visualization for a graphical user interface.
- Support for move validation, legal moves, and game-over detection.

---

## Directory Structure
```plaintext
.
├── images/                 # Chess piece images
├── LICENSE                 # Project license
├── my_chess.py             # Console-based chess engine integration
├── README.md               # Project overview and usage instructions
├── requirements.txt        # Python dependencies
├── src/                    # Source code
│   ├── assets/             # Asset management
│   │   ├── __init__.py
│   │   └── loader.py       # Handles loading of assets like images
│   ├── core/               # Game core logic
│   │   ├── engine.py       # Handles Stockfish and game state
│   │   ├── game.py         # Main game coordination logic
│   │   └── __init__.py
│   ├── main.py             # Entry point for the Pygame-based application
│   └── ui/                 # User interface logic
│       ├── board.py        # Handles drawing and interaction with the board
│       ├── utils.py        # UI utility functions
│       └── __init__.py
└── tests/                  # Unit and integration tests
    ├── test_board.py       # Tests for board rendering and interaction
    ├── test_engine.py      # Tests for engine integration
    ├── test_game.py        # Tests for game coordination logic
Current Implementation
1. Console-Based Game (my_chess.py)
Interactive chess game against Stockfish with move input/output through the console.
Uses chess.Board for game state and chess.engine.SimpleEngine for AI interaction.
Move validation and game-over checks implemented.
2. Pygame Visualization
Planned as the next phase, integrating Pygame for graphical visualization of the chessboard.
Highlights:
Modular board and UI components.
Support for mouse input to select and move pieces.
Development Roadmap
Phase 1: Console Implementation ✅
Implemented a functional chess game playable in the terminal.
Phase 2: Pygame Visualization 🚧
Create a graphical chessboard.
Integrate chess.Board logic with the Pygame layer.
Add drag-and-drop or click-based piece movement.
Phase 3: Enhancements
AI difficulty levels using Stockfish.
Online multiplayer support.
UI polish and additional game features (e.g., move history, undo).
Requirements
Python 3.8+
Libraries:
pygame
python-chess
To install dependencies:

bash
Copy code
pip install -r requirements.txt
Running the Game
Console Version
Run the terminal-based game:

bash
Copy code
python my_chess.py
Pygame Version (To Be Implemented)
Run the graphical interface:

bash
Copy code
python src/main.py
Contributing
Contributions are welcome! Please ensure all new code is well-documented and tested. Submit pull requests to the dev branch.