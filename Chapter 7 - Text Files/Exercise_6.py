import random

def main():
    random_number = random.randint(1,10)
    with open(f"Python-Exercises\Chapter 7 - Text Files\FilesChapter7\wish{random_number}.txt") as file:
        print(f"Wish {random_number}\n")
        for line in file:
            print(line.rstrip())


if __name__ == "__main__":
    main()