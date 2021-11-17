sentence = ""

for i in range(5):
    word = input("Enter word {}: ".format(i+1)).capitalize()
    sentence = word + " " + sentence
print("The words in reversed order are:\n" + sentence)