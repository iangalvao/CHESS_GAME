# Chess Game Project

## Overview
This project is a Python-based chess game that allows players to compete against the Stockfish engine. Initially designed as a console-based application, it is structured to evolve into a graphical chess game with Pygame integration. The codebase emphasizes modularity and scalability for future features like enhanced AI, multiplayer support, and an intuitive UI.

---

## Features
- Interactive chess game against Stockfish.
- Console-based interface.
- Modular architecture for clean code and future enhancements.

---

## Directory Structure
```
.
├── .gitignore             # Files and directories to ignore in Git
├── LICENSE                # Project license
├── README.md              # Project overview and usage instructions
├── requirements.txt       # Python dependencies
├── src/                   # Source code
│   ├── core/              # Core game logic
│   ├── ui/                # User interface components
│   └── main.py            # Main entry point for the application
├── tests/                 # Unit and integration tests
└── images/                # Graphics for Pygame (planned)
```

---

## Requirements
- Python 3.8 or newer
- Libraries:
  - `python-chess`
  - `pygame` (for future graphical features)

To install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage
### Console Version
Run the game in the terminal:
```bash
python src/main.py
```

---

## Contributing
Contributions are welcome! Please follow these guidelines:
1. Ensure all code is well-documented and tested.
2. Submit pull requests to the `dev` branch.

---

## Roadmap
- [x] Console-based chess game
- [ ] Pygame integration for graphical UI
- [ ] AI difficulty levels
- [ ] Online multiplayer support
- [ ] Enhanced UI with features like move history and undo options

---

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

## Acknowledgments
- `python-chess` library for robust chess logic.
- Stockfish for providing a powerful chess engine.

---

