import random

a = random.randint(1, 6)

b = input("Guess a number from 1 to 6:")
b = int(b)

print(a == b)