# A
def main():
    
    with open("D:\OneDrive\Documents\Python-Exercises\Chapter 7 - Text Files\FilesChapter7\hamlet.txt") as file:
        with open("hamlet2.txt", "w") as file2:
            lines = file.readlines()
            for line in lines:
                for char in ",.?!;:":
                    line = line.replace(char+"  ", char+" ")
                file2.write(line)


if __name__ == '__main__':
    main()