text = input("What do you eat for lunch: ")

if text.count("sandwich") == 2:
    word = text[text.find("sandwich")+8:]
    word_word = word[:word.find("sandwich")]
    print("You have", word_word, "between your sandwich.")
else: 
    print("")