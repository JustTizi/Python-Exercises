def Caps_and_Lowers(input_string):
    counter_lower = counter_upper = 0
    for i in range(len(input_string)):
        if input_string[i].isupper():
            counter_upper += 1
        elif input_string[i].islower():
            counter_lower += 1
    return  [counter_upper, counter_lower]

sentence = input("Your string: ")

caps_and_lowers = Caps_and_Lowers(sentence)

print("Number of capitals:", caps_and_lowers[0])
print("Number of lowercase letters:", caps_and_lowers[1])

password = input("Set your password (at least 2 uppercase and 2 lowercase letters): ")
caps_and_lowers = Caps_and_Lowers(password)

while caps_and_lowers[0] < 2 or caps_and_lowers[1] < 3:
    password = input("Set your password (at least 2 uppercase and 2 lowercase letters): ")
    caps_and_lowers = Caps_and_Lowers(password)