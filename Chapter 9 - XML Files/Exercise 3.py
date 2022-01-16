import xml.etree.ElementTree as ET

def main():
	count = 1
	xmlDoc = ET.parse("D:\OneDrive\Documents\Python-Exercises\Chapter 9 - XML Files\Files chapter 9\jobs.xml")
	root = xmlDoc.getroot()
	print("Overview IT Vacancies:\n")

	for company in root.find("jobs"):
		name = company[0].text
		contact = company[1].find("email").text
		
		for vacancy in company.find("vacancies"):
			if vacancy[0].get("group") == "IT":
				count_text = str(count) + "."
				print(f"{str(count_text).ljust(6)}{'Position:'.ljust(12)}{vacancy[0].text}")
				print(f"{''.ljust(6)}{'Company:'.ljust(12)}{name}")
				print(f"{''.ljust(6)}{'Contact:'.ljust(12)}{contact}")
				count += 1
			print()


if __name__ == '__main__':
	main()