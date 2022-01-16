def main():
	with open("D:\OneDrive\Documents\Python-Exercises\Chapter 8 - Group Data\Files chapter 8\classrooms.txt") as file:
		line = file.readline().rstrip()
		record = line.split(';')

		while line:
			members = 0
			classroom = record[2]
			print(classroom)

			while line and record[2] == classroom:
				if line != '\n':
					members += 1
					print(f"\t{record[1]} {record[0]}")
					line = file.readline().rstrip()
					record = line.split(';')

			print(f"Number of students in classroom {classroom} = {members}")

if __name__ == '__main__':
	main()