def main():
    i = 1
    with open("D:\OneDrive\Documents\Python-Exercises\Chapter 7 - Text Files\Exercise_10.py", "r") as input_file:
        with open("output_file.txt", "w") as output_file:
            for line in input_file:
                output_file.write(f"{str(i).rjust(4)} {line}")
                i += 1

if __name__ == '__main__':
    main()