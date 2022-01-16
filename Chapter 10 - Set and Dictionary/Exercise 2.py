def main():
	first_names_1itf = set()
	first_names_2itf = set()

	with open("D:\OneDrive\Documents\Python-Exercises\Chapter 10 - Set and Dictionary\Files Chapter 10\\first_names1ITF.txt", encoding='utf-8') as itf1:
		with open("D:\OneDrive\Documents\Python-Exercises\Chapter 10 - Set and Dictionary\Files Chapter 10\\first_names2ITF.txt", encoding='utf-8') as itf2:
			
			for line in itf1:
				if line != '\n':
					first_names_1itf.add(line.rstrip())

			for line in itf2:
				if line != '\n':
					first_names_2itf.add(line.rstrip())

			print(f"In 1ITF there are {len(first_names_1itf)} different first names.")
			print(f"In 2ITF there are {len(first_names_2itf)} different first names.")
			name_intersection= first_names_1itf.intersection(first_names_2itf)

			print(f"There are {len(name_intersection)} first names appearing in 1ITF and 2ITF.")
			for name in name_intersection:
				print(name)


if __name__ == '__main__':
	main()