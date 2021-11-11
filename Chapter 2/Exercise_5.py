number = int(input("Enter a number: "))

if number < 0:
    print("Negative numbers will not be tested")
else:
    final_digit = int(input("What final digit do you want to test with: "))
    if final_digit == number % 10:
        print(number, "ends with", final_digit)
    else:
        print(number, "does not end with", final_digit)