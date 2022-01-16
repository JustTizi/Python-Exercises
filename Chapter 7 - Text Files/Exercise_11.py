def main():
    with open("D:\OneDrive\Documents\output_file.txt", "r") as input_file:
        with open("output_file_no_number.txt", "w") as output_file:
            for line in input_file:
                output_file.write(f"{line[5:]}")

if __name__ == "__main__":
    main()