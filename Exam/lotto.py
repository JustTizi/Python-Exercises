import random


def pick_lotto_balls(amount):
    list_of_rolls = []
    while amount != 0:
        random_number = random.randint(1, 20)
        if list_of_rolls.count(random_number) == 0:
            list_of_rolls.append(random_number)
            amount -= 1
    list_of_rolls.sort()
    return list_of_rolls


rolls = int(input("How many balls do you want to pick? "))


while rolls > 20 or rolls < 1:
    print("You should give a number from 1 to 20.")
    rolls = int(input("How many balls do you want to pick? "))

random_list = pick_lotto_balls(rolls)
correct_guesses = 0

for i in range(1, 6):
    guess = int(input("Guess " + str(i) + " "))
    if guess in random_list:
        correct_guesses += 1

if correct_guesses == 0:
    print("No correct answers, keep on trying ;-)")
else:
    print("Number of correct answers:", str(correct_guesses) + ".")

print("The numbers in the barrel:", *random_list)