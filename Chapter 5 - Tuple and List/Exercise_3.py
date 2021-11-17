original_list = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]
print("Original list:", original_list)

for i in range(len(original_list)-1):
    original_list.insert(0, original_list[-1])
    original_list.pop(-1)

print("After sliding:", original_list)