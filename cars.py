cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list: ")
print(str(cars) + "\n")

print("Here is the sorted list: ")
print(str(sorted(cars)) + "\n")
print(str(sorted(cars, reverse = True)) + "\n")

print("Here is the original list again: ")
print(str(cars) + "\n")

cars = ["bmw", "audi", "toyota", "subaru"]
cars.reverse()
print(cars)
print(len(cars))