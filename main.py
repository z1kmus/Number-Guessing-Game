import random
import os

difficulties = {
    1: 10,
    2: 5,
    3: 3,
}

def generateNumber():
    randomNumber = random.randint(1, 100)
    return randomNumber


def intro():
    print("Please select the difficulty level:")
    print("[1] Easy (10 chances)")
    print("[2] Medium (5 chances)")
    print("[3] Hard (3 chances)")
    userChoice = int(input("\nEnter your choice: ").strip())
    return userChoice

def printUserGuesses(arr):
    print("Guessed num/s:", end=' ')
    for num in arr:
        if num == arr[-1]:
            print(num, end='      ')
        else:
            print(num, end=', ')

def main():
    numOfGuesses = difficulties[intro()]
    print("\nGreat! You have selected the Medium difficulty level.")
    print(f"You have {numOfGuesses} chances to guess the correct number.")
    print("\nI'm thinking of a number between 1 and 100.")
    print("I'm ready! Let's start the game!")
    print("=" * 60)
    num = generateNumber()
    attempt = 0
    guessed_nums = []

    while True:
        if attempt >= numOfGuesses:
            print(f"Game Over! The number was {num}")
            print("=" * 60)
            break
        else:
            if len(guessed_nums) != 0:
                printUserGuesses(guessed_nums)
                print(f"Attempts left: {numOfGuesses - attempt}\n")
            attempt += 1
            userGuess = int(input("Enter your guess: "))
            print()
            if userGuess < 100 and userGuess >= 1:
                if userGuess > num and attempt != numOfGuesses:
                    print(f"Incorrect! The number is less than {userGuess}.")
                elif userGuess < num and attempt != numOfGuesses:
                    print(f"Incorrect! The number is greater than {userGuess}.")
                elif userGuess == num:
                    print(f"Congratulations! You guessed the correct number in {attempt} attempts.")
                    print("=" * 60)
                    break
                if attempt != numOfGuesses:
                    print("=" * 60)
                if userGuess not in guessed_nums:
                    guessed_nums.append(userGuess)
            else:
                print("Please enter numbers between 1 and 100!")
    again = input("Do you want to play again? (y/n): ").lower()
    if again == 'y' or again == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')




if __name__ == '__main__':
    print("=" * 60)
    print("Welcome to the Number Guessing Game!".center(60))
    print("=" * 60)
    main()