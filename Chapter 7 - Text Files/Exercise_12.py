from random import randint

def main():
    random_number = randint(1, 10)
    with open(f"table_{random_number}.txt", "w") as file:
        for i in range(1, 11):
            if i == 10:
                file.writelines(f"{i}x{random_number}={i*random_number}")
            else:
                file.writelines(f"{i}x{random_number}={i*random_number}\n")


if __name__ == '__main__':
    main()