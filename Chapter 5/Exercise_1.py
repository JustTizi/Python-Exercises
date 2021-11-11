original_list = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]


print("Original list: \t", original_list)

original_list.insert(0, original_list[-1])
original_list.pop(-1)
original_list.append(original_list[1])
original_list.pop(1)
print("After the switch: \t", original_list)
