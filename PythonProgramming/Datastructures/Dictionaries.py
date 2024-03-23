#Dictionaries are unordered collections of items. Each item in a dictionary has a key-value pair. Dictionaries are mutable, and the keys are unique within a dictionary.

# Creating a dictionary
person = {"name": "John", "age": 30, "city": "New York"}
print(person)

# Accessing a value by key
print(person["name"])  # Outputs: John

# Adding a new key-value pair
person["email"] = "john@example.com"
print(person)

# Removing a key-value pair
del person["age"]
print(person)
