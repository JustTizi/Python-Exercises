colour = input("What is your favourite colour: ")
j = 0
print(colour[:3:2])

print("This colour consists of", len(colour), "letters")
print()

for i in range(len(colour)):
    print(colour[i], "=", ord(colour[i]))
print()

while j < len(colour):
    if j % 2 == 0:
        print("#" + colour[j] + "#")
    else:
        print("**" + colour[j] + "**")
    j += 1