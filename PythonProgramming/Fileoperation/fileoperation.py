from pathlib import Path
#reading the files 

#file writing the contnet 
text_to_write = """Hello, Python!
This is an example of writing text to a file.
Each line is separated by a newline character.\n"""

#append example
text_to_append=" append on the file"



# Reading the entire content at once
with open('Fileoperation/example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('Fileoperation/example.txt', 'r') as file:
    for line in file:
        print(line, end='')  # The end='' parameter prevents adding an extra newline since 'line' already ends with one

# writing text to a file
with open('Fileoperation/example.txt', 'w') as file:
    file.write(text_to_write)

print(f"Text has been written to example.txt")

# writing text to a file
with open('Fileoperation/example.txt', 'a') as file:
    file.write(text_to_append)

print(f"Append has been written to example.txt")