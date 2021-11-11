initial_limit = int(input("Initial limit: "))
final_limit = int(input("Final limit: "))

if final_limit < initial_limit:
    print("The initial limit must be smaller than the final limit!")
elif initial_limit == final_limit:
    print("Sum of numbers from", initial_limit, "till", final_limit)
    print(initial_limit)
else:
    print("Sum of numbers from", initial_limit, "till", final_limit)
    for i in range(initial_limit+1, final_limit+1):
        initial_limit += i
        print("+", i, "-->", initial_limit)