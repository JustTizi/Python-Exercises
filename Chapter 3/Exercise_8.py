final_digit = int(input("What final digit do you want to check the numbers on: "))
running_count = 0

for i in range(0, 10):
    number = int(input("Enter a number: "))
    if number % 10 == final_digit:
        running_count += 1
if running_count == 1:
    print("1 out of 10 numbers ends on", final_digit)
else:
    print(running_count, "out of 10 numbers end on", final_digit)