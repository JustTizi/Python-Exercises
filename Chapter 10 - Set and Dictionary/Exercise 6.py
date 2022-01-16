def main():
	animal_sounds = {}
	score = 0

	with open("D:\OneDrive\Documents\Python-Exercises\Chapter 10 - Set and Dictionary\Files Chapter 10\\animal_sounds.txt") as sounds:
		for line in sounds:
			animal_makes = line.rstrip().split(";")
			
		print("Do you know the animal sounds?")
		for animal in animal_sounds:
			guess = input(f"What is the sound of a {animal.lower()}? ")
			if guess == animal_sounds[animal]:
				score += 1
		print(f"You have {score} correct answers.")


if __name__ == '__main__':
	main()