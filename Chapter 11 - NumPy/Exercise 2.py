import numpy as np

def main():
	python = np.genfromtxt('D:\OneDrive\Documents\Python-Exercises\Chapter 11 - NumPy\Files_Chapter_11\points_python.txt', delimiter=';', filling_values='0')
	network = np.genfromtxt('D:\OneDrive\Documents\Python-Exercises\Chapter 11 - NumPy\Files_Chapter_11\points_networks.csv', delimiter=';', filling_values='0')
	web = np.loadtxt('D:\OneDrive\Documents\Python-Exercises\Chapter 11 - NumPy\Files_Chapter_11\points_web.txt', delimiter=';')
	linux = np.loadtxt('D:\OneDrive\Documents\Python-Exercises\Chapter 11 - NumPy\Files_Chapter_11\points_linux.csv', delimiter=';')

	total = (python + network + web + linux)/4
	print(total)
	total[:,1] *= 5
	print(total)
	title_string = "November 2021 Exam results:"

	print(title_string)
	print(len(title_string)*"_")
	print(f"The highest score this exam period is: {np.max(total[:,1], axis=0)}%")
	print(f"The lowest score this exam period is: {np.min(total[:,1], axis=0)}%")


if __name__ == '__main__':
    main()