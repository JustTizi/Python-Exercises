files = int(input("How many files? "))

for i in range(1, files+1):
	open(f"Exercise {i}.py", "x")
	open_file = open(f"Exercise {i}.py", "w")
	open_file.write("def main():\n\t\n\nif __name__ == '__main__':\n\tmain()")