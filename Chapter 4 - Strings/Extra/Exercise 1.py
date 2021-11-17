word = original_word = "shafik is dik"
hidden_word = ""
for i in range(len(word)):
    if word[i] != " ":
        hidden_word += "#"
    elif word[i] == " ":
        hidden_word += " "

print("You have to guess this quote:", hidden_word)
letter_guess = input("Guess a letter or press / if you think you know the quote: ")

while letter_guess != "/" and "#" in hidden_word:
    if "#" in hidden_word:
        while letter_guess in word:
            hidden_word = hidden_word[:word.find(letter_guess)] + letter_guess + \
                          hidden_word[word.find(letter_guess) + 1:]
            word = word[:word.find(letter_guess)] + "#" + word[word.find(letter_guess) + 1:]
    print("You already have this result:", hidden_word)
    letter_guess = input("Guess another letter: ")

if letter_guess == "/":
    word_guess = input("OK. You think you know, just say it. ")
    if word_guess == original_word:
        print("Yes, you win!")
    else:
        print("Unlucky, you lose")

if hidden_word == original_word:
    print("Yes you win")