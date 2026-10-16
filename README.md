# Number Guessing Game

This project is a number guessing game written in Python. The player tries to guess a hidden number between 1 and 100 within a limited number of attempts.

Project URL -> https://roadmap.sh/projects/number-guessing-game

## About the Game

- There are 3 difficulty levels:
  - Easy — 10 attempts
  - Medium — 5 attempts
  - Hard — 3 attempts
- The player's guess is compared with the hidden number.
- If the guess is too high, the game tells the user the number is smaller.
- If the guess is too low, the game tells the user the number is larger.
- The game ends when the player guesses correctly or runs out of attempts.

## Project Structure

```text
NumberGuessingGame/
├── main.py
├── README.md
└── .gitignore
```

## Requirements

- Python 3.8 or higher

## How to Run the Game

1. Open your terminal or command prompt.
2. Go to the project folder:

```bash
cd /Users/mustafo/Desktop/Projects/NumberGuessingGame
```

3. Run the following command:

```bash
python main.py
```

## Gameplay

1. The program asks the user to choose a difficulty level.
2. The number of attempts is selected based on the chosen level.
3. The player guesses a number between 1 and 100.
4. The program gives hints such as "too high" or "too low".
5. If the player guesses correctly, they win.

## Example

```text
Welcome to the Number Guessing Game!
Please select the difficulty level:
[1] Easy (10 chances)
[2] Medium (5 chances)
[3] Hard (3 chances)
Enter your choice: 2

Great! You have selected the Medium difficulty level.
You have 5 chances to guess the correct number.
```

## Author

This project was created for learning Python and practicing basic game development.

Made with ❤️ by z1kmus.

## License

This project is intended for personal learning and educational use.
