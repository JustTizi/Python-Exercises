count = 0
with open("D:\\School\\Python Essentials 1\\Python-Exercises\\Chapter 7 - Text Files\\FilesChapter7\\first_names.txt", "r") as file:
    while file:
        print(file.readline())
        count += 1