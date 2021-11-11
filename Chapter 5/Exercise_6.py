text = input("Enter a text: ").lower()
letters = []

for i in range(len(text)):
    if text[i] != " " and not text[i] in letters:
        letters.append(text[i])
letters.sort()
print(letters)
print(*letters)
print(*letters, sep="\t")