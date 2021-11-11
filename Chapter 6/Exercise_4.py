import random

#ex a
def generate_list(rolls, start_of_die, end_of_die):
    list_of_rolls = []
    for i in range(rolls):
        list_of_rolls.append(random.randint(start_of_die, end_of_die))
    return list_of_rolls

#ex b
def filter(input_list):
    new_list = []
    for i in range(len(input_list)):
        if new_list.count(input_list[i]) == 0:
            new_list.append(input_list[i])
    return new_list

#ex c
amount_of_rolls = int(input("How many dice do you want to roll? "))
generated_numbers = generate_list(amount_of_rolls, 1, 6)

print("You threw", generated_numbers)
print("Your unique rolls were:", filter(generated_numbers))

#ex c poker
poker_rolls = []
counter = 1
while len(filter(poker_rolls)) != 1:
    poker_rolls = generate_list(10, 1, 20)
    print("You threw:", poker_rolls, sep="\t")
    counter += 1
print("You threw poker after", counter, "times.")