yes_votes = int(input("How many people voted YES? "))
no_votes = int(input("How many people voted NO? "))
blank_votes = int(input("How many people left a BLANK vote? "))

total_votes = yes_votes + no_votes + blank_votes

yes_percent = (yes_votes/total_votes)*100
no_percent = (no_votes/total_votes)*100
blank_percent = (blank_votes/total_votes)*100

print("Percentage of yes votes: " + str(yes_percent) + "%")
print("Percentage of no votes: " + str(no_percent) + "%")
print("Percentage of blank votes: " + str(blank_percent) + "%")