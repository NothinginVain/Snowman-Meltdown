from game_logic import play_game

def main():
    """
    Run the main game loop.

    Starts the game once, then repeatedly asks the user if they want
    to play again. If the user enters 'y', the game restarts. If the
    user enters 'n', the program exits. Any other input prompts the
    user to try again.
    """

    play_game()
    while True:
        play_again = input(
            "Do you want to play again ? if yes type 'y' if "
            "no type 'n': ").lower().strip()
        if play_again == "y":
            play_game()
            continue

        if play_again == "n":
            print("By, by. ")
            return
        else:
            print("invalid input,, try again ")
            continue

if __name__ == "__main__":
    main()
