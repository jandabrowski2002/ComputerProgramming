import math

a = input("Enter the lenght of side a:")
b = input("Enter the lenght of side b:")
c = input("Enter the lenght of side c:")

a = float(a) 
b = float(b)
c = float(c)

p = (a+b+c) / 2

area = math.sqrt((p*(p-a)*(p-b)*(p-c)))#**0.5

print(f"The area of this triangle is: {area}")
