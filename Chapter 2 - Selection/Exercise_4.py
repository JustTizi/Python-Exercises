number_one = int(input("Number 1: "))
number_two = int(input("Number 2: "))
number_three = int(input("Number 3: "))

if number_one - number_two - number_three == 0:
    print("This works")
elif number_two - number_one - number_three == 0:
    print("This works")
elif number_three - number_two - number_one == 0:
    print("This works")
else:
    print("This won't work")