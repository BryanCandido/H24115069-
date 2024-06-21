import random
import string

def display_histogram(guesses):
    print("Guess Histogram:")
    frequency = {}
    for guess in guesses:
        frequency[guess] = frequency.get(guess, 0) + 1
    for guess, count in frequency.items():
        print(f"{guess}: {'*' * count}")

def main():
    alphabet = random.choice(string.ascii_lowercase)
    guesses = []
    tries = 0

    while True:
        guess = input("Guess the lowercase alphabet: ")
        tries += 1

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a lowercase alphabet.")
            continue

        guesses.append(guess)

        if guess == alphabet:
            print(f"Congratulations! You guessed the alphabet in {tries} tries.")
            print("Your guesses:", guesses)
            display_histogram(guesses)
            break
        elif guess < alphabet:
            print("The aLphabet you are looking for is alphabetically higher. ")
        else:
            print("The aLphabet you are looking for is alphabetically lower. ")

if __name__ == "__main__":
    main()
