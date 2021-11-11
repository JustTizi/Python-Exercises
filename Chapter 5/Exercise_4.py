original_tuple = (2, 3, 9, 1, 5, 7, 3, 4)
i = len(original_tuple) - 1

print(original_tuple)

if 4 in original_tuple:
    while original_tuple[i] != 4:
        i -= 1

    new_tuple = (original_tuple[i+1:])
    print(new_tuple)
else:
    print("The number 4 does not appear in the Tuple")
