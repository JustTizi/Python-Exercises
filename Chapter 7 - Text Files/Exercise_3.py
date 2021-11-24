def main():
    with open("D:\\School\\Python Essentials 1\\Python-Exercises\\Chapter 7 - Text Files\\FilesChapter7\\first_names.txt", "r") as file:
        line = file.readlines()
        counter = 0
        while counter < len(line):
            print(line[counter].rstrip().ljust(13), end = '')
            counter += 1
            if counter % 10 == 0:
                print()
if __name__ == '__main__':
    main()