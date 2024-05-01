import random
import string
import turtle

# Load words from a file (e.g., words.txt)
def load_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [word.strip() for word in file]

# Remove punctuation and convert to lowercase
def preprocess_word(word):
    return ''.join(char.lower() for char in word if char.isalpha())

# Compare Latvian letters to ASCII equivalents
def normalize_letter(letter):
    latvian_to_ascii = {
        'ā': 'a',
        'č': 'c',
        'ē': 'e',
        'ģ': 'g',
        'ī': 'i',
        'ķ': 'k',
        'ļ': 'l',
        'ņ': 'n',
        'š': 's',
        'ū': 'u',
        'ž': 'z'
    }
    return latvian_to_ascii.get(letter, letter)

# Choose a random word from the list
def choose_word(word_list):
    return random.choice(word_list)

# Initialize the game
def hangman_game():

    word_list = load_words('HangMan_words.txt')  # Replace with your word file
    mode = input("Choose a mode (single or duo): ").lower()

    if mode == 'single':
        chosen_word = choose_word(word_list)
    elif mode == 'duo':
        chosen_word = input("Enter the secret word: ").lower()
    else:
        print("Invalid mode. Please choose 'single' or 'duo'.")
        return
    
    guessed_letters = set()
    attempts = 9  # Number of allowed incorrect guesses
    correct_guesses = 0

    print("Welcome to Hangman!")
    print(f"Guess the word (length: {len(chosen_word)})")

    while attempts > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in chosen_word])
        print(f"\nWord: {display_word}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Please enter a single valid letter.")
            continue

        guess = normalize_letter(guess)

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:
            print("Correct guess!")
            correct_guesses += chosen_word.count(guess)
        else:
            attempts -= 1
            print(f"Incorrect guess! You have {attempts} attempts left.")
            # Draw a part of the hangman using turtle
            # (You can customize this part based on your preference)

        if correct_guesses == len(chosen_word):
            print(f"Congratulations! You guessed the word: {chosen_word}")
            break

    else:
        print(f"Game over! The word was: {chosen_word}")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again == 'yes':
        hangman_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    hangman_game()
