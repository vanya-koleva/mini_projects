# BTS-Themed Rock, Paper, Scissors Game

This Python script implements a simple Rock, Paper, Scissors terminal-based game against a computer opponent. The game is a classic two-player game where each player chooses one of three options: rock, paper, or scissors. The winner is determined by the following rules:

* Rock smashes scissors.
* Paper covers rock.
* Scissors cut paper.

## Requirements
* Python 3.x
* colorama library

## Code Overview
### Imports and Initialization
The game begins by importing the following modules:

* random for generating random numbers.
* unicodedata for accessing Unicode characters.
* time for adding sleep intervals between actions.
* colorama for adding color to the terminal output.

### Game Setup
* The game initializes with a list of BTS members' names for the computer opponent, randomly chosen from a predefined list.
* The game uses special Unicode characters for Rock, Paper, and Scissors, and color codes for visual appeal.

### Game Loop
* The game runs in an infinite loop until the player decides to quit.
* Each round, the player is prompted to choose a move, and the computer's move is randomly generated.
* The game determines the winner based on the rules of Rock, Paper, Scissors.
* After each round, the player is asked if they want to play again.

### Scoring
* The game keeps track of the player's and computer's scores.
* The final scores are displayed at the end of the game.
### Exit
* The game can be exited by entering an invalid input for the player's move or by choosing not to play again.

## Example Output
![rock_paper_scissors_example_output](https://github.com/vanya-koleva/mini_projects/blob/main/rock_paper_scissors/rock_paper_scissors_example_output.png?raw=true))

## Live Demo
[Replit](https://replit.com/@Vanya-Koleva/rockpaperscissors)
