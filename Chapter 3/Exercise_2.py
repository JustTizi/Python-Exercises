number = int(input("Enter a number: "))
zeroes = sixes = 0


while number > 0:

    if number % 10 == 0:
        zeroes += 1
    elif number % 10 == 6:
        sixes += 1

    number = number // 10

    

print("The number consists of", zeroes, "zeroes and", sixes, "sixes")