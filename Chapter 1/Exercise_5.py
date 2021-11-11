current_exchange_rate = float(input("Enter the current exchange dollar rate (€ -> $): "))
euro_amount = float(input("Enter your amount in euro: "))
dollar_amount = euro_amount * current_exchange_rate

print(euro_amount, "€ = ", dollar_amount, "$")