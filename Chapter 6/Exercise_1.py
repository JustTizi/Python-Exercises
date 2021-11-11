def Celcius_to_Fahrenheit(Celcius):
    Fahrenheit = Celcius * 1.8 + 32
    return Fahrenheit

celcius = float(input("Degrees Celcius: "))

print(celcius, "degrees Celcius =", Celcius_to_Fahrenheit(celcius), "degrees Fahrenheit")