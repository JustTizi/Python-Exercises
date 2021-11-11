a = int(input("number 1 (0, 1 or 2): "))
b = int(input("number 2 (0, 1 or 2): "))
c = int(input("number 3 (0, 1 or 2): "))

if a == b and b == c:
    if a == 2:
        print("10")
    else:
        print("5")
elif a != b and b == c:
    print("1")
else:
    print("0")