amount = input("Enter amount:")
amount = float(amount)

vat = (amount)*0.23
vat = round(vat, 2)

print(f"VAT paid: {vat}")
