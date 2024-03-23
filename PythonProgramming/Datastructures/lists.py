#Lists are ordered, mutable (changeable) collections of items. Items in a list can be of any data type

# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Adding an item to the list
fruits.append("orange")
print(fruits)

fruits.append(1.56)
# Accessing an item by its index
print(fruits[1])  # Outputs: banana

# Slicing a list
print(fruits[1:3])  # Outputs: ['banana', 'cherry']

print(fruits)
