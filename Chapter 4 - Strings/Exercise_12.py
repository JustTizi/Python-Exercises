text = input("Enter a string: ")
pos = text.find("*")

while pos != -1:
    text = text[:pos-1] + text[pos+2:]
    pos = text.find("*")
    
print(text)