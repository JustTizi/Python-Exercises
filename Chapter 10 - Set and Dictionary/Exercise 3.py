def main():
	classrooms = set()
	with open("D:\OneDrive\Documents\Python-Exercises\Chapter 10 - Set and Dictionary\Files Chapter 10\local_booking.txt", "r") as file:
		print("Classrooms:")
		for line in file:
			classrooms.add(line.rstrip().split(";")[3])
	for classroom in classrooms:
		print(classroom)

if __name__ == '__main__':
	main()