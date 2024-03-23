#set
#Sets are unordered collections of unique items. They are mutable and are useful for removing duplicate elements from a collection or performing mathematical set operations like union, intersection, difference, and symmetric difference.
# Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Adding an item to the set
fruits.add("orange")
print(fruits)

# Adding a duplicate item (will have no effect because sets only contain unique items)
fruits.add("apple")
print(fruits)

# Set operations
vegetables = {"carrot", "potato", "cucumber"}
all_items = fruits.union(vegetables)
print(all_items)
