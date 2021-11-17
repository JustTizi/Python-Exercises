birth_year = int(input("Enter your birth year: "))
age = 2021 - birth_year

if age >= 18:
    print("Your age =", age)
    print("So you're an adult.")
else:
    print("Your age =", age)
    print("You're not an adult yet.")