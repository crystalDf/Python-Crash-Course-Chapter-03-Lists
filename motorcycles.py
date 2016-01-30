motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles.insert(1, 'yamaha')
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.append(popped_motorcycle)
print(motorcycles)

first_owned = motorcycles.pop(0)
print(motorcycles)
print(first_owned)

motorcycles.insert(0, first_owned)
motorcycles.append('ducati')
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)