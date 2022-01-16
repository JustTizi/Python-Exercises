def main():
	days_in_months = {
		"January": "31",
		"February": "28",
		"March": "31",
		"April": "30",
		"May": "31",
		"June": "30",
		"July": "31",
		"August": "31",
		"September": "30",
		"October": "31",
		"November": "30",
		"December": "31"
	}

	month_input = input("Month (press Enter if you want to see an overview of all months): ")
	if month_input in days_in_months:
		print(days_in_months[month_input])
	elif month_input == "":
		for month in days_in_months:
			print(f"{month.ljust(9)}\t{days_in_months[month]}")
	else:
		print("This month does not exist.")


if __name__ == '__main__':
	main()