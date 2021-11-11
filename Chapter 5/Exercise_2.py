number_list = [23, 12, 54, 85, 46, 30, 26, 64, 91]
new_list = []

for i in range(len(number_list)):
    if number_list[i] % 2 == 0:
        new_list.append(number_list[i])
        
for i in range(len(number_list)):
    if number_list[i] % 2 != 0:
        new_list.append(number_list[i])
print(number_list, "becomes", new_list)