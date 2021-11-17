import random

computer_pick = random.randint(0, 50)
player_pick = -1
count = 0
while player_pick != computer_pick:
    player_pick = int(input("Enter a positive number: "))
    count += 1
    if player_pick < computer_pick:
        print("Higher")
    elif player_pick > computer_pick:
        print("Lower")

print("You have guessed the number", computer_pick, "in", count, "turns.")
