first_number = int(input("First number: "))
second_number = int(input("Second number: "))

if 30 <= first_number <= 40 and 30 <= second_number <= 40:
    print("Both numbers are ok")
elif first_number == 65 or first_number == 72 or first_number == 83 or first_number == 90:
    if second_number == 65:
        print("Both numbers are ok")
    elif second_number == 72:
        print("Both numbers are ok")
    elif second_number == 83:
        print("Both numbers are ok")
    elif second_number == 90:
        print("Both numbers are ok")
    else:
        print("They are NOT ok")
else:
    print("They are NOT ok")
