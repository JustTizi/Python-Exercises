def EUR_to_USD(eur, conversion):
    usd = eur * conversion
    return usd

conversion_rate = float(input("Current dollar rate (€ -> $): "))
eur_amount = float(input("Your amount in Euro: "))

print("€", eur_amount, "= $", EUR_to_USD(eur_amount, conversion_rate))