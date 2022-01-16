def main():
	with open("D:\OneDrive\Documents\Python-Exercises\Chapter 8 - Group Data\Files chapter 8\courses.csv", "r") as input_file:
		with open("students.csv", "w") as output_file:
			line = input_file.readline()
			line = input_file.readline().rstrip()
			record = line.split(";")

			while line:
				student_nr = record[4]
				courses = []

				data = f"{record[3]};{record[4]};{record[5]}"
				courses.append(data)
				while line and record[4] == student_nr:
					if line != "\n":
						courses[0] = courses[0] + f";{record[1]} ({record[2]})"
						line = input_file.readline().rstrip()
						record = line.split(";")
				courses[0] = courses[0] + "\n"
				output_file.write(*courses)

if __name__ == '__main__':
	main()