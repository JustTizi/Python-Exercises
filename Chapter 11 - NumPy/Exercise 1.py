import numpy as np

def main():
	grades = np.loadtxt("D:\OneDrive\Documents\Python-Exercises\Chapter 11 - NumPy\Files_Chapter_11\student_grades_3.csv", delimiter=";", skiprows=1)
	min_grades = np.min(grades, axis=0)
	max_grades = np.max(grades, axis=0)
	mean_grades = np.mean(grades, axis=0)
	print("Grades analysis Python:")
	print(f"{max_grades[0]}\tmin {min_grades[0]}\tmean {mean_grades[0]}")
	print("Grades analysis Linux:")
	print(f"{max_grades[1]}\tmin {min_grades[1]}\tmean {mean_grades[1]}")
	print("Grades analysis Routing & Switching:")
	print(f"{max_grades[2]}\tmin {min_grades[2]}\tmean {mean_grades[2]}")

if __name__ == '__main__':
	main()