import xml.etree.ElementTree as ET

def main():
	xmlDoc = ET.parse("D:\OneDrive\Documents\Python-Exercises\Chapter 9 - XML Files\Files chapter 9\drugs.xml")
	root = xmlDoc.getroot()

	for leaflet in root.findall("leaflet"):
		leaflet.find("name").text = leaflet.find("name").text.upper()
		leaflet.remove(leaflet.find("pharmaceutical_forms"))
	xmlDoc.write("drugs_changed.xml")

if __name__ == '__main__':
	main()