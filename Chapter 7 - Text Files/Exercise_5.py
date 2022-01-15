def main():
    with open("Python-Exercises\Chapter 7 - Text Files\FilesChapter7\\books.txt") as file:
        counter = 1
        for line in file:
            print(f"{counter}. {line.rstrip()} --> ", end="")
            print(file.readline().rstrip())
            counter += 1


if __name__ == "__main__":
    main()