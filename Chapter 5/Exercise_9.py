names = []
distances = []
print("Enter your name and the distance to school.")
print("Type stop when you want to close the entry.")
name = input("Your name: ")

while name != "stop":
    distance = float(input("Distance to school: "))
    names.append(name)
    distances.append(distance)
    name = input("Your name: ")

if len(names) != 0:
    print("Overview")
    for i in range(len(names)):
        print(names[i], distances[i], sep="\t")
    print(names[distances.index(max(distances))], "lives fathest, namely", max(distances), "km")
    print("The average distance is", sum(distances)/len(distances))
