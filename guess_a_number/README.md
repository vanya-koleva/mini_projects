# BTS-Themed Guess the Number Game
This Python script is a simple number guessing game where the player competes against a computer, trying to guess a computer-generated number. The game is designed to be challenging, with the difficulty increasing as the player progresses through levels. The game uses the random, time, and unicodedata libraries for generating random numbers, tracking time, and displaying special characters, respectively. Additionally, it utilizes the colorama library for colored terminal output, enhancing the game's visual appeal.

## Requirements
* Python 3.x
* colorama library

## Game Overview
The game starts by selecting a random name from a predefined list of names, which is then displayed in a colorful format. The player is then challenged to guess a number that the computer has in mind. The game lasts for one minute, and the player's score is calculated based on the number of levels they reach and the number of attempts it takes to guess the correct number.

## Game Mechanics
### Initialization
* The game initializes by selecting a random name from a list of BTS members'names and displays it in a colorful format.
* The game then prints a challenge message, informing the player that they have one minute to guess as many numbers as possible.
### Gameplay
* The game is divided into levels, with each level increasing the maximum number the player can guess.
* The player is prompted to guess a number within the current level's range.
* If the player's guess is correct, they are congratulated, and their score is updated.
* If the guess is too high or too low, the player is informed accordingly.
* The game continues until the player runs out of time or decides to quit.
### Scoring
* The player's score is calculated based on the number of levels reached and the number of attempts it takes to guess the correct number.
* The player's score is displayed after each correct guess.
### End of Game
* The game ends when the time limit is reached. The player is informed of their final score and the level they reached.

## Example Output
![guess_the_number_example_output](https://github.com/vanya-koleva/mini_projects/blob/main/guess_a_number/guess_the_number_example_output.png?raw=true)

## Live Demo
[Replit](https://replit.com/@Vanya-Koleva/guessthenumber)
