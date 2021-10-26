x = input("Enter the x coordinate:")
y = input("Enter the y coordinate:")

x = int(x)
y = int(y)

if x>0 and y>0:
    print(f"Point ({x}, {y}) is in the first quadrant")

if x<0 and y>0:
    print(f"Point ({x}, {y}) is in the second quadrant")
    
if x<0 and y<0:
    print(f"Point ({x}, {y}) is in the third quadrant")
    
if x>0 and y<0:
    print(f"Point ({x}, {y}) is in the fourth quadrant")