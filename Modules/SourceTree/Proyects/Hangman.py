import random
word_list = ["Rio Bucana", "Rio Inabon", "Rio Jacaguas", "Rio Grande de Manati", "Rio Grande de Arecibo", "Rio Espiritu Santo", "Rio Matilde",
"Rio Grande de Loiza", "Rio Guajataca", "Rio Cibuco" ]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hand Hangman")
    print("Theme: Los Rios de Puerto Rico")
    print(display_hangman(tries))
    print(word_completion)
    [print("\n")]
    while not guessed and tries > 0:
        guess = input("Guess a letter or word").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already tried",guess, "!")
            elif guess not in word:
                print("Isnt in the word :(")
                tries -= 1
                guessed_letters.append(guess)

def display_hangman(tries):
 stages = [ """
 --------
 | |
 | O
 |/|\\
 | |
 |/ \\
 -
 """,
 """
 --------
 | |
 | O
 |/|\\
 | |
 |/
 -
 """,
 """
 --------
 | |
 | O
 |/|\\
 | |
 |
 -
 """,
 """"
 --------
 | |
 | O
 |/|
 | |
 |
 -
 """,
 """
 --------
 | |
 | O
 | |
 | |
 |
 -
 """,
 """
 --------
 | |
 | O
 |
 |
 |
 -
 """,
 """
 --------
 | |
 |
 |
 |
 |
 -
 """,
 ]