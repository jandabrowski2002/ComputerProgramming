num1 = input("Enter first number:")
num2 = input("Enter the second number:")
num1 = int(num1)
num2 = int(num2)

if num1 > num2 :
    print(f"Numbers in ascending order: {num2}, {num1}")

if num2 > num1 :
    print(f"Numbers in ascending order: {num1}, {num2}")


if num2 == num1 :
    print("Those numbers are equal!")