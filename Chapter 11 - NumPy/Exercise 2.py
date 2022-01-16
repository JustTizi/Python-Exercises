import numpy as np

def main():
	python_scores = np.genfromtxt("D:\OneDrive\Documents\Python-Exercises\Chapter 11 - NumPy\Files_Chapter_11\points_python.txt", delimiter=";", filling_values="10")
	network_scores = np.genfromtxt("D:\OneDrive\Documents\Python-Exercises\Chapter 11 - NumPy\Files_Chapter_11\points_networks.csv", delimiter=";", filling_values="10")
	web_scores = np.genfromtxt("D:\OneDrive\Documents\Python-Exercises\Chapter 11 - NumPy\Files_Chapter_11\points_web.txt", delimiter=";", filling_values="10")
	linux_scores = np.genfromtxt("D:\OneDrive\Documents\Python-Exercises\Chapter 11 - NumPy\Files_Chapter_11\points_linux.csv", delimiter=";", filling_values="10")

	for i in range(100)
		averages = np.array([python_scores[i][1], network_scores[i][1], web_scores[i][1], linux_scores[i][1]])

	print(averages)


if __name__ == '__main__':
	main()