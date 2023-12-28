Reversi (Othello) in Python
===========================

This project is an implementation of the classic board game Reversi (also known as Othello) in Python, using the Pygame library. It features an on-screen menu for selecting game modes, automated turn skipping when no valid moves are available, and a winner announcement at the end of the game.

Getting Started
---------------

Prerequisites
-------------

Before running the game, ensure you have Python and the Pygame library installed on your system. To install Pygame, use pip:

    pip install pygame

Running the Game
----------------

Clone this repository and run the Reversi.py file to start the game:

    git clone https://github.com/Divycholera98/reversi.git
    cd reversi
    python Reversi.py

Game Modes
----------

- Two Player Mode: Two players take turns on the same machine.
- Play Against Computer: Challenge an AI opponent. The AI uses alpha-beta pruning for decision-making.

Gameplay
--------

1. Launch the game.
2. Select the desired mode by clicking on the corresponding button on the screen.
3. Players take turns placing a disk on the board.
4. Capture the opponent's disks by trapping them between your disks.
5. The game ends when the board is full or no valid moves are available.
6. The winner is displayed at the end of the game.

Skipping Turns
--------------

If a player has no valid moves, their turn is automatically skipped.

Controls
--------

- Use the mouse to click on the board to place your disk.
