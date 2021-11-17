#r0889630 Tiziano Van der Waals 1ITF3

word = input("Enter a word: ").lower()
ignore = input("Which character should be ignored: ").lower()
ignore_count = len(word)

for i in range(len(word)):
    if word[i] != ignore:
        word = word.replace(word[i], "+")
        ignore_count -= 1
print("Result:", word)

if ignore_count == 0:
    print("No characters were ignored.")
elif ignore_count == 1:
    print("The character '" + ignore + "' was ignored 1 time.")
else:
    print("The character '" + ignore + "' was ignored", ignore_count, "times.")