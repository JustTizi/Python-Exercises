def main():
    women = []
    men = []
    with open("D:\OneDrive\Documents\Python-Exercises\Chapter 7 - Text Files\FilesChapter7\contacts.csv") as file:
        for line in file:
            if line.rstrip().split(";")[3] == "M":
                men.append(line.rstrip().split(";"))
            else:
                women.append(line.rstrip().split(";"))

        women = sorted(women, key=lambda x: x[1])
        men = sorted(men, key=lambda x: x[1])

        print(f"{len(women)} girls:")
        for person in women: 
            print(f"\t{person[1]} {person[0]}")

        print(f"{len(men)} men:")
        for person in men: 
            print(f"\t{person[1]} {person[0]}")


if __name__ == '__main__':
    main()


#  Better solution
#  
#  boys = []
#  girls = []
#  
#  with open('../Chapter Files/contacts.csv') as file:
#      line = file.readline()
#      while line:
#          record = line.split(";")
#          if record[3].rstrip() == 'M':
#              boys.append(record[1] + ' ' + record[0])
#          else:
#              girls.append(record[1] + ' ' + record[0])
#          line = file.readline()
#  
#  boys.sort()
#  girls.sort()
#  
#  print(len(girls), "girls:")
#  for girl in girls:
#      print('\t', girl)
#  
#  print(len(boys), "boys:")
#  for boy in boys:
#      print('\t', boy)
    
