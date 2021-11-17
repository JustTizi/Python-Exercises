name = input("Give name (press enter to stop): ")

while name != "":
    new_name = ""
    print("Menu:", "*"*5, "U Uppercase", "L Lowercase", "A Alternate", sep="\n")

    choice = input("Make a choice (U-L-A): ")

    while choice != "U" and choice != "L" and choice != "A" and choice != "u" and choice != "l" and choice != "a":
        choice = input("Make a choice (U-L-A): ")

    if choice == "U" or choice == "u":
        print(name.upper())
    elif choice == "L" or choice == "l":
        print(name.lower())
    elif choice == "A" or choice == "a":
        for i in range(len(name)):
            if i % 2 == 0:
                new_name += name[i].upper()
            else:
                new_name += name[i].lower()
        print(new_name)
    print()
    name = input("Give name (press enter to stop): ")
