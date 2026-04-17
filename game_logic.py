import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown", "html", "code"]


def get_random_word():
    """Return a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Show the snowman stage and return the hidden word display."""
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    return display_word


def game_validation(guess_char, guess_letters_list):
    """Check if the user's guess is valid.

        Raise ValueError if the input is empty, too long,
        not a letter, or already guessed.
        """
    if len(guess_char) == 0:
        raise ValueError("Invalid input, please type a letter")

    if len(guess_char) > 1:
        raise ValueError("Invalid input, you only can type one letter, "
                         "try again")

    if not guess_char.isalpha():
        raise ValueError("Invalid input. Please type a letter fom A to Z")

    if guess_char in guess_letters_list:
        raise ValueError("You already guessed that letter.")


def play_game():
    """Run the Snowman Meltdown game until the player wins or loses."""
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    guess_letters_list = []
    max_mistakes = len(STAGES) - 1

    while True:
        status_result = (display_game_state
                         (mistakes, secret_word, guess_letters_list))
        print(status_result)

        if all(letter in guess_letters_list for letter in secret_word):
            print(f"Congratulations, you saved the snowman!")
            print()
            break

        try:
            guess_char = input("Guess a letter: ").lower().strip()
            game_validation(guess_char,guess_letters_list)
        except ValueError as error:
            print(error)
            continue

        print("You guessed:", guess_char)
        guess_letters_list.append(guess_char)

        if guess_char not in secret_word:
            print("Wrong letter!")
            mistakes += 1
        else:
            print("You found one secret letter!")

        if mistakes >= max_mistakes:
            print(STAGES[mistakes])
            print(f"Game Over! The word was: {secret_word}")
            break

