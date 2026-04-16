import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown", "html", "code"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    return display_word


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    guess_letters_list = []
    max_mistakes = len(STAGES) - 1

    while True:
        status_result = display_game_state(mistakes, secret_word, guess_letters_list)
        print(status_result)

        if "_" not in status_result:
            print(f"Congratulations, you saved the snowman!")
            break

        guess_char = input("Guess a letter: ").lower()
        print("You guessed:", guess_char)

        if guess_char in guess_letters_list:
            print("You already guessed that letter.")
            continue
        guess_letters_list.append(guess_char)

        if guess_char not in secret_word:
            mistakes += 1

        if mistakes >= max_mistakes:
            print(STAGES[mistakes])
            print(f"Game Over! The word was: {secret_word}")
            break

if __name__ == "__main__":
    play_game()