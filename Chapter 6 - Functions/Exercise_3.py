def print_square(number, character):
    for i in range(number):
        for j in range(number):
            print(character, end="")
        print()
    return None

character_to_use = input("Which character must be used to form the lines (enter = stop): ")

while character_to_use != "":
    number_of_lines = int(input("Number of characters per line = number of lines = "))
    print_square(number_of_lines, character_to_use)
    character_to_use = input("Which character must be used to form the lines (enter = stop): ")
    