import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors :")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices =  {"player": player_choice, "computer": computer_choice}
    return choices

def test():
    return 0

def check_win(player, computer):
    print(f"you choose: {player}, computer choose: {computer} ")
    if player == computer:
        return "It is a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! YOU WIN!"
        else:
            return "Paper covers rock! YOU LOSE!"
    elif player == "paper": 
        if computer == "rock":
            return "Paper covers rock! YOU WIN!"
        else:
            return "rock covers paper! YOU LOSE!"
    elif player == "scissors": 
        if computer == "paper":
            return "Scissors cuts paper! YOU WIN!"
        else:
            return "Rock smahses scissor! YOU LOSE!"
        

choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
