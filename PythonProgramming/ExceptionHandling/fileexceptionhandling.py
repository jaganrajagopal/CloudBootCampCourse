
try:
    file = open('file.txt', 'r')
    print ("try to open the files")
except FileNotFoundError:
    print("File not found.")
finally:
    print("This block is executed no matter what.")
    # Make sure you check if 'file' exists before trying to close it
    
    
    #file.close()