import random
def main():
    print("Welcome to Rock, Paper, Scissors Game")
    RPS = ["rock", "paper", "scissors"]
    play_again = "y"

    while play_again == "y":
        playerChoice = input("Lets play. Choose one: rock, paper, or scissors.\n")
        computerChoice = random.choice(RPS)

        print(f"Computer selected: {computerChoice}")
        print(f"Player selected: {playerChoice}")

        if(playerChoice == computerChoice):
            print("You tied :/")
        elif(playerChoice == "rock" and computerChoice == "paper"):
            print("Papers covers Rock. You lost!!! :( ")
        elif(playerChoice == "paper" and computerChoice == "scissors"):
            print("You lost")
        elif(playerChoice == "rock" and computerChoice == "scissors"):
            print("You Win")
        elif(playerChoice == "paper" and computerChoice == "rock"):
            print("You Win")
        elif(playerChoice == "scissors" and computerChoice == "paper"):
            print("You Win")
        else:
            print("somethnig isn't right. Maybe try again")
        play_again = input("Play again? Enter 'y' for yes or 'n' for no\n")
    print("Game Concluded.")
main()