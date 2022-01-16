import xml.etree.ElementTree as ET

def main():
    xmlDoc = ET.parse("D:\School\Python Essentials 1\Python-Exercises\Chapter 9 - XML Files\Files chapter 9\cinemas.xml")
    root = xmlDoc.getroot()
    print("Bioscopen in Antwerpen")
    for bioscoop in root.findall("bioscoopoverzicht"):
        if bioscoop.find("district").text == "Antwerpen":
            naam = bioscoop.find("naam").text
            adres = bioscoop.find("straat").text + " " + bioscoop.find("huisnummer").text
            plaats = bioscoop.find("postcode").text + " " + bioscoop.find("district").text.upper()
            print(f"{naam}\n{adres}\n{plaats}")
            print()


if __name__ == '__main__':
    main()