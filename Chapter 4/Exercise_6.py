string = input("Enter a string: ")
new_string = ""

for i in range(len(string)):
        if i % 3 == 0:
            if len(string[i:]) >= 3:
                new_string += string[i+1:i+3] + string[i]
            else:
                new_string += string[i:]
print(new_string)