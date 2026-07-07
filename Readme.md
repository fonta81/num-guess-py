# Number Guessing Game

A simple and interactive terminal-based Number Guessing Game written in Python. The program generates a random number between 1 and 20, and the player has to guess it based on proximity hints.

## Features

- **Dynamic Hints:** Tells the user if their guess is too high or too low.
- **Proximity Detection:** Provides a unique hint ("Very close...") if the guess is within 5 units of the correct number.
- **Input Validation:** Handles invalid inputs (such as text or out-of-bounds numbers) smoothly without crashing the game.
- **Interactive Menu:** A clean main menu that allows players to play multiple rounds or exit at any time.

## Game Rules

1. The game selects a secret random integer between 1 and 20.
2. You input your guess when prompted.
3. If your guess is incorrect, you will receive a hint to help you adjust your next choice.
4. The game continues until you find the correct number!

## Requirements

- Python 3.x

## How to Run

1. Clone or download this repository.
2. Save the script as `Adivina.py`.
3. Open your terminal or command prompt, navigate to the directory where the file is saved, and run:

```bash
python Adivina.py
