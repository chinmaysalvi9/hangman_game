from collections import defaultdict

WORD = "secret"


def hangman():
    allowed_errors = 7
    unlocked_word = ["_"] * len(WORD)

    remaining = defaultdict(list)

    for index, character in enumerate(WORD):
        remaining[character].append(index)

    already_guessed = set()

    while True:
        print("Enter guess character")
        character = input()

        if len(character) > 1 or not character.isalpha():
            print("Not valid character. Try again.")
            continue

        elif character in already_guessed:
            print("Already guessed correctly. Try another alphabet")

        elif character in remaining:

            for index in remaining[character]:
                unlocked_word[index] = character

            del remaining[character]

        elif allowed_errors:
            print(f"Incorrect Guess. Remaining allowed errors are {allowed_errors}")
            allowed_errors -= 1

        else:
            print("Game Over.")

        print("".join(unlocked_word))

        if len(remaining) == 0:
            print("You won.")
            break


if __name__ == "__main__":
    hangman()
