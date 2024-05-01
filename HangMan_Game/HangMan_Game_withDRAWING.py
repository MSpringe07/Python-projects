import random
import string
import turtle

def draw_hangman(attempts):
    t = turtle.Turtle()
    t.speed(0)  # Set turtle speed to fastest
    if attempts < 9:
        t.circle(50)
    if attempts < 8:
        t.right(90)
        t.forward(200)
    if attempts < 7:
        t.right(22)
        t.forward(150)
    if attempts < 6:
        t.penup()
        t.goto(0, -200)
        t.pendown()
        t.left(44)
        t.forward(150)
    if attempts < 5:
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.right(44)
        t.forward(150) 
    if attempts < 4:
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.left(44)
        t.forward(150)  
    if attempts < 3:
        t.penup()
        t.goto(-150, -330)
        t.pendown()
        t.right(22)
        t.backward(500)  
    if attempts < 2:
        t.left(90)
        t.forward(150)
    if attempts < 1:
        t.right(90)
        t.forward(70)

# Load words from a file (e.g., words.txt)
def load_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [word.strip() for word in file]

# Remove punctuation and convert to lowercase
def preprocess_word(word):
    return ''.join(char.lower() for char in word if char.isalpha())

# Choose a random word from the list
def choose_word(word_list):
    return random.choice(word_list)
    
# Initialize the game
def hangman_game():
    word_list = load_words('Hangman_words.txt')  # Replace with your word file
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

        if guess == "stop game":
            break

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Please enter a single valid letter.")
            continue

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
            draw_hangman(attempts)
            # (You can customize this part based on your preference)

        if correct_guesses == len(chosen_word):
            print(f"Congratulations! You guessed the word: {chosen_word}")
            break

    else:
        print(f"Game over! The word was: {chosen_word}")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again == 'yes' or play_again == 'y':
        hangman_game()
    elif play_again == 'no' or play_again == 'n':
        print("Thanks for playing!")
    else:
        print("You cannot follow simple instructions! I hope you have a horrible day :)")

if __name__ == "__main__":
    hangman_game()
