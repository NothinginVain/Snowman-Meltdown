from game_logic import play_game

def main():
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
            break
        else:
            print("invalid input,, try again ")
            continue

if __name__ == "__main__":
    main()
