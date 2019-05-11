from enum import Enum
import random

class Options(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Result(Enum):
    WIN = 1
    LOSS = 2
    DRAW = 3

def player_decision():
    choice = Options(int(input("1: Rock\n2: Paper\n3: Scissors\nYour choice: ")))
    print("You chose " + choice.name.lower() + ".")
    return choice

def computer_decision():
    choice = random.choice(list(Options))
    print("Computer chose " + choice.name.lower() + ".")
    return choice

def compare_choices(player_choice, computer_choice):
    if player_choice == computer_choice:
        return Result.DRAW
    elif player_choice == Options.ROCK and computer_choice == Options.SCISSORS:
        return Result.WIN
    elif computer_choice == Options.ROCK and player_choice == Options.SCISSORS:
        return Result.LOSS
    elif player_choice.value < computer_choice.value:
        return Result.LOSS
    else:
        return Result.WIN

def main():
    player_score = computer_score = draw = 0
    while(True):
        player_choice = player_decision()
        computer_choice = computer_decision()
        result = compare_choices(player_choice, computer_choice)

        if result == Result.WIN:
            print("You win")
            player_score += 1
        elif result == Result.LOSS:
            print("You lose")
            computer_score += 1
        else:
            print("Draw")
            draw += 1

        print("===== Result =====")
        print("Total: " + str(player_score + computer_score + draw))
        print("Player: " + str(player_score))
        print("Computer: " + str(computer_score))
        print("Draw: " + str(draw))
        print("==================")

if __name__ == '__main__':
    main()