number_one = int(input("Number 1: "))
number_two = int(input("Number 2: "))
number_three = int(input("Number 3: "))

if number_one < number_two and number_one < number_three:
    print("The smallest number is", number_one)
elif number_two < number_one and number_two < number_three:
    print("The smallest number is", number_two)
elif number_three < number_one and number_three < number_two:
    print("The smallest number is", number_three)
elif number_one > number_two and number_two == number_three:
    print("The smallest number is", number_three)
elif number_two > number_one and number_one == number_three:
    print("The smallest number is", number_three)
elif number_three > number_one and number_one == number_two:
    print("The smallest number is", number_two)
else:
    print("All your numbers are the same")

