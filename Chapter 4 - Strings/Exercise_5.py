text = input("Enter a text: ")
triple_count = 0

for i in range(len(text)):
    if text[i] == text[i-1] and text[i] == text[i-2]:
        triple_count += 1

if triple_count == 1:
    print("There is", triple_count, "triple in this text")
elif triple_count == 0:
    print("There are no triples in this text")
else:
    print("There are", triple_count, "triples in this text")