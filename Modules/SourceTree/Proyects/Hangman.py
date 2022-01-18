import random
word_list = ["Rio Bucana", "Rio Inabon", "Rio Jacaguas", "Rio Grande de Manati", "Rio Grande de Arecibo", "Rio Espiritu Santo", "Rio Matilde",
"Rio Grande de Loiza", "Rio Guajataca", "Rio Cibuco" ]
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