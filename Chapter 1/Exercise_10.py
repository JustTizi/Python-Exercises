fixed_annual_amount = 83.6
night_per_kwh = .035
day_per_kwh = .068
vat = .21

consumption_day = int(input("Power consumption during the day (kilowatt per hour): "))
consumption_night = int(input("Power consumption during the night (kilowatt per hour): "))

price_day = day_per_kwh * consumption_day
price_night = night_per_kwh * consumption_night

price_total_ex_vat = price_day + price_night + fixed_annual_amount
price_total_incl_vat = price_total_ex_vat + (price_total_ex_vat * vat)

print("Invoice \n *******")
print("Fixed costs: € ", fixed_annual_amount)
print("Daily consumption: € ", price_day)
print("Night consumption: € ", price_night)
print("Total excluding vat: € ", price_total_ex_vat)
print("Total including vat: € ", price_total_incl_vat)