bottles_of_wine = int(input("How many bottles of wine are there: "))
pizzas = int(input("How many pizzas are there: "))


if pizzas > 5 and bottles_of_wine > 5:
    if bottles_of_wine >= 2 * pizzas or pizzas >= 2 * bottles_of_wine:
        print("This is a fantastic party")
    else:
        print("This is a good party")
else: 
    print("This is just a stupid party")