number_one = int(input("First number: "))
number_two = int(input("Second number: "))

if number_one < 0:
    number_one = 0 - number_one

if number_two < 0:
    number_two = 0 - number_two

if number_one % 5 == 0 and number_two % 5 == 0:
    if number_one > number_two:
        print("The answer for the numbers", number_one, "and", number_two , "=", number_two)
    elif number_two > number_one:
        print("The answer for the numbers", number_one, "and", number_two , "=", number_one)
    else:
        print("The answer for the numbers", number_one, "and", number_two , "= 0")
else:
    if number_one > number_two:
        print("The answer for the numbers", number_one, "and", number_two , "=", number_one)
    elif number_two > number_one:
        print("The answer for the numbers", number_one, "and", number_two , "=", number_two)
    else:
        print("The answer for the numbers", number_one, "and", number_two , "= 0")
