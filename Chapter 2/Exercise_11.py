weight_in_kg = float(input("Your weight in kilograms: "))
length_in_cm = float(input("Your length in centimeters: "))

bmi = weight_in_kg / (length_in_cm ** 2) * 10000

print("A person of", weight_in_kg, "kg with a length of", length_in_cm, "cm has as BMI", bmi)

if bmi < 18:
    print("This is underweight.")
elif 18 <= bmi < 25:
    print("This is a normal weight.")
elif 25 <= bmi < 27:
    print("This is slightly overweight.")
elif 27 <= bmi < 30:
    print("This is moderately overweight.")
elif 30 <= bmi < 40:
    print("You are obese.")
else:
    print("You are sickly obese.")