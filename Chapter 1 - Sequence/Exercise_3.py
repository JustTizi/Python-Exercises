three_number_digit = int(input("Enter a three-digit number: "))
half_digit = three_number_digit/2
double_digit = three_number_digit*2
third_power_digit = three_number_digit**3
tenfold_digit = three_number_digit*10

digit_one = three_number_digit // 100
digit_two = (three_number_digit % 100) // 10
digit_three = three_number_digit % 10

print("Half = " + str(half_digit))
print("Double = " + str(double_digit))
print("Third power = " + str(third_power_digit))
print("Tenfold = " + str(tenfold_digit))
print("The digits are: \n" + str(digit_one) + "\n" + str(digit_two) + "\n" + str(digit_three))