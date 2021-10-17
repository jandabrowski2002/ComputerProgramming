weight = input("Enter your weight:")
weight = float(weight)
height = input("Enter your height:")
height = float(height)

result = ((weight) / ((height) ** 2))*10000

result = round(result, 2)

print(f"Your BMI is: {result}")

