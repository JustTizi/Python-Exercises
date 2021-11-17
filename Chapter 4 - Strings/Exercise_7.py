text = input("Enter a text: ")

length_counter = final_counter = 1

for i in range(1, len(text)):
    
    if text[i] == text[i-1]:
        length_counter += 1
    else:
        final_counter = max(final_counter, length_counter)
        length_counter = 1

final_counter = max(final_counter, length_counter)

print("The length of the longest block in this text is", final_counter)