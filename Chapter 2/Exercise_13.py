computer_choice = "scissors"
player_choice = input("What do you choose: rock, paper or scissors? ")

print("You chose", player_choice)
print("I chose", computer_choice)

if player_choice == "rock":
    if computer_choice == "rock":
        print("it's a tie :-|")
    elif computer_choice == "paper":
        print("You lose :-(")
    elif computer_choice == "scissors":
        print("You win :-)")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("You lose :-(")
    elif computer_choice == "paper":
        print("it's a tie :-|")
    elif computer_choice == "scissors":
        print("You win :-)")
elif player_choice == "scissors":
    if computer_choice == "rock":
        print("You lose :-(")
    elif computer_choice == "paper":
        print("You win :-)")
    elif computer_choice == "scissors":
        print("it's a tie :-|")
else:
    print("That's an incorrect choice")
