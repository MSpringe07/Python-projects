# Hangman Game

This Python script runs a game of Hangman. The game can be played in single or duo mode.

## Features

1. In single mode, the script chooses a random word from a list of words.
2. In duo mode, one player enters a secret word and the other player guesses it.
3. The script draws a hangman using the turtle library each time a player makes an incorrect guess.
4. The game continues until the player guesses the word or the hangman is fully drawn.

## How to Run

You can run this script using Python 3. Make sure you have the `random`, `string`, and `turtle` libraries installed. If not, you can install them using pip:

\`\`\`bash
pip install turtle
\`\`\`

Then, you can run the script:

\`\`\`bash
python script_name.py
\`\`\`

Replace `script_name.py` with the name of the script file.

## Output

The script prints the current state of the word after each guess. If the player guesses the word, the script prints a congratulatory message. If the player fails to guess the word, the script prints a game over message.

The script also asks the player if they want to play again after each game.

## Note

The script uses the turtle library to draw the hangman. The turtle library opens a new window for the drawing. Please make sure that your environment supports opening new windows.
