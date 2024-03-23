#a tuple is a collection which is ordered and immutable (unchangeable). Tuples can contain items of different data types, such as strings, integers, and even other tuples. Here's an example demonstrating how to create tuples with a combination of strings and integers, 
#including multiple sets of these combinations:

# A simple tuple with a string and an integer
simple_tuple = ("apple", 5)

# A tuple containing multiple sets of strings and integers
multi_set_tuple = (("banana", 2), ("orange", 3), ("grapes", 50))

# Nested tuples, where each element is a tuple of a string and an integer
nested_tuples = (("bread", 1), ("milk", 2), ("eggs", 12))

# A mix of strings, integers, and tuples
mixed_tuple = ("watermelon", 1, ("blueberry", 20), "strawberry", 15)

# You can not add the elements ( Immutable )
tuplesset = {(1, 2, 3,'j')}  # A set with a tuple
tuple_to_add = (4, 5, 6 ,4.5)
tuplesset.add(tuple_to_add)  # This works
print("tupleset adding elements")
print(tuplesset)

# Accessing elements in tuples
print(simple_tuple[0])  # Output: apple
print(multi_set_tuple[1])  # Output: ('orange', 3)
print(nested_tuples[2][1])  # Output: 12
print(mixed_tuple[2])  # Output: ('blueberry', 20)