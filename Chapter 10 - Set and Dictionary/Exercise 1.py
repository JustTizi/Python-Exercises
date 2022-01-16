def main():
	number_set = set()
	letter_set = set()
	input_string = input("Enter a text consisting only of letters and numbers: ")
	for char in input_string:
		if char in "0123456789":
			number_set.add(char)
		else:
			letter_set.add(char)
	print("The numbers are: ")
	for number in number_set:
		print(number)
	print("The letters are: ")
	for letter in letter_set:
		print(letter)

if __name__ == '__main__':
	main()