number = product = 1
count = 0

while number != 0:
    number = int(input("Enter a number, stop by entering zero: "))
    if number != 0:
        product *= number
        count += 1

print("The product of the", count, "numbers is", product)