# part a b
# def main():
#     count = 0
#     with open("Python-Exercises\\Chapter 7 - Text Files\\FilesChapter7\\first_names.txt", "r") as file:
#         line = file.readline()
#         while line:
#             if line != "\n":
#                 print(line.rstrip("\n"))
#                 count += 1
#             line = file.readline()
#         print(f"There are {count} first names in the file.")

#part c
def main():
    count = 0
    z_count = 0
    with open("Python-Exercises\\Chapter 7 - Text Files\\FilesChapter7\\first_names.txt", "r") as file:
        line = file.readline()
        while line:
            if line != "\n":
                count += 1
                if "z" in line.lower():
                    print(line.rstrip())
                    z_count += 1
            line = file.readline()
        print(f"There are {count} first names in the file.\
            \n{z_count} of which contain a letter z.")

if __name__ == "__main__":
    main()
