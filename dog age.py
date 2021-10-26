dog_age = input("Enter your dog age in human years:")
dog_age = int(dog_age)

if dog_age <= 2:
    result = dog_age * 10.5
    result = int(result)
    print(f"Your dog is {result} years old in dog years")

if dog_age > 2:
    result = 2*10.5+((dog_age-2)*4)
    result = int(result)
    print(f"Your dog is {result} years old years")