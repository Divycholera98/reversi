
Reversi (Othello) in Python
===========================

This project is an implementation of the classic board game Reversi (also known as Othello) in Python, utilizing the Pygame library. It offers both a two-player mode and an AI mode where you can play against the computer.

Getting Started
---------------

Prerequisites
-------------

Before running the game, you need to have Python installed on your system along with the Pygame library. If you don't have Pygame installed, you can install it via pip:

    pip install pygame

Running the Game
----------------

To play the game, simply clone this repository and run the Reversi.py file:

    git clone [Your-Repository-URL]
    cd [Your-Repository-Name]
    python Reversi.py

Game Modes
----------

1. Two-Player Mode: In this mode, two players take turns on the same machine.
2. AI Mode: Play against an AI opponent. The AI uses an alpha-beta pruning algorithm for decision-making.

Gameplay
--------

- Launch the game.
- Select the desired mode (Two-Player or AI Mode).
- In the game, players will alternate turns, placing one disk on the board with each turn.
- The goal is to capture the opponent's disks by trapping them between your own.
- The game ends when the board is full or no valid moves are available.
- The player with the most disks on the board at the end of the game wins.

Controls
--------

- Use the mouse to click on the board where you want to place your disk.
