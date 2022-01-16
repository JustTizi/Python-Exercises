import xml.etree.ElementTree as ET

def main():
    xmlDoc = ET.parse("D:\School\Python Essentials 1\Python-Exercises\Chapter 9 - XML Files\Files chapter 9\plants.xml")
    root = xmlDoc.getroot()
    counter = 1

    #ex a
    #for plant in root.findall("plant"):
    #    common = plant.find("common").text
    #    botanical = plant.find("botanical").text.capitalize()
    #    print(f"Plant {counter}: {common} ({botanical})")
    #    counter += 1

    for plant in root.findall("plant"):
        if plant[3].text == "SUN":
            common = plant.find("common").text
            botanical = plant.find("botanical").text.capitalize()
            print(f"Plant {counter}: {common} ({botanical})")
            counter += 1


if __name__ == '__main__':
    main()