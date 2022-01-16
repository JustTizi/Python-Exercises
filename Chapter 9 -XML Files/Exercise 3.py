import xml.etree.ElementTree as ET

def main():
	count = 0
	xmlDoc = ET.parse("D:\OneDrive\Documents\Python-Exercises\Chapter 9 -XML Files\Files chapter 9\jobs.xml")
	root = xmlDoc.getroot()
	print("Overview IT Vacancies:\n")
	for company in root.iter("company"):
		count_text = str(count) + "."
		position = company.iter("vacancy")
		all_positions = position
		if all_positions.attrib() == "IT":
			print(f"{str(count_text).ljust(6)}\t \
				{'Position:'.ljust(12)}\t \
					{all_positions.text()}")
			print(f"{''.ljust(6)}\t \
				{'Company:'.ljust(12)}\t \
					{company.find('name').text()}")
			print(f"{''.ljust(6)}\t \
				{'Contact:'.ljust(12)}\t \
					{company.iter('email').text()}")
			print()


if __name__ == '__main__':
	main()