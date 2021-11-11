number = int(input("Enter a number: "))

for i in range(number, 0, -1):

    print(number, "... ".format(i), end="")
    number -= 1
print("0")
    