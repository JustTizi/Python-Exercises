number = int(input("Enter a number: "))
largest = 0
smallest = 0

if number != 0:

    while number != 0:
        if largest < number:
            largest = number
        elif smallest > number:
            smallest = number
        number = int(input("Enter a number: "))

difference = largest - smallest
print("The difference between the largest number", largest, "and the smallest", smallest, "=", difference)