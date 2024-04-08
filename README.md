# Pygame Mastermind
A classic code-breaking game, Mastermind, under development using Python, Pygame, pygame_menu and tkinter, with a custom-designed UI and logo.

## Key Features
* Intuitive UI: Easy-to-navigate menus and gameplay visuals powered by Pygame and pygame_menu.
* Classic Mastermind Logic: Faithful implementation of the original game rules.
* Adjustable Difficulty in terminal version: Customize the number of code slots and colors.

## Prerequisites
* Python 3.x
* Pygame
* pygame_menu
* tkinter

## Installation
```Bash
# Creates a virtual environment and installs dependencies
bash build_venv.sh
```
## Running the Game

```Bash

# For terminal gameplay:
python  pygame2d/mstmdn_secret/mastermind_logic.py

# For UI gameplay (still under development):
python pygame2d/main_menu.py

```
## How to Play
* Secret Code: The computer (or another player in a future multiplayer mode?) generates a secret code of colored pegs.
* Code Breaking: The player attempts to guess the secret code by placing colored pegs in successive rows.
* Feedback: The game provides hints, indicating the number of pegs that are the correct color and in the correct position, and the number that are the correct color but in the wrong position.
* Victory: The player wins by guessing the secret code within the allotted number of turns.

## Game Structure (Technical)
* UI: pygame_menu handles menus, Pygame manages game graphics. tkinter will enable board game photo upload for future computer vision functionality
* Game Logic: A core Mastermind class (or function) handles code generation, feedback, and win conditions.

## Screenshots 
| Image 1                               | Image 2                               |
| ------------------------------------- | ------------------------------------- |
| [Image of options screen](pygame2d/assets/Options.PNG) | [Image of gameplay screen](pygame2d/assets/game_ss.PNG) | 


## Future Development
* Connect UI to game logic.
* Enhanced Difficulty Options: Implement variable difficulty settings.
* Sound effects: For a more immersive experience
* Computer Vision: Allow user to upload photo of a board game
