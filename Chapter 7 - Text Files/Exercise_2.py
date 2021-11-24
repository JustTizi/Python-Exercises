def main():
    with open("D:\\School\\Python Essentials 1\\Python-Exercises\\Chapter 7 - Text Files\\FilesChapter7\\first_names.txt", "r") as file:
        names = file.readlines()
    print(*names[::-1])
    

if __name__ == '__main__':
    main()