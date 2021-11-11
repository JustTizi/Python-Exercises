numbers = [42, 18, 0, 37, 0, 2, 19, 10, 5, 14]

print(numbers)

for index in range(len(numbers)-1):
    if numbers[index] == 0:
        largest_odd_number = 0
        for i in range(index+1, len(numbers)):
            if numbers[i] % 2 != 0 and numbers[i] > largest_odd_number:
                largest_odd_number = numbers[i]
        numbers[index] = largest_odd_number
print(numbers)