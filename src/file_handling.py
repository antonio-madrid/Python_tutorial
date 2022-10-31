# ------------------------------------------------------------------------------------------------------
# Open files in a classic way
# ------------------------------------------------------------------------------------------------------

# open() must be in a try block and also need to be closed
try:
    f = open("../support/demofile.txt")  # 'rt' as a second parameter by default
    data = f.read()  # read() loads all data in a file
    print("Printing all the data in a try block:")
    print(data)
    f.close()
except IOError:
    print("Cannot open the file")


# ------------------------------------------------------------------------------------------------------
# Open files using 'with open' function
# ------------------------------------------------------------------------------------------------------

# with open() is a sugar syntax, avoiding the use of try block and close() function
# file must be named with an alias
with open("../support/demofile.txt") as file:
    partial_data = file.read(5)
    print("Printing partial data")
    print(partial_data)

    # readline() allows to load a full line
    print("printing lines:")
    print(file.readline())
    print(file.readline())


# ------------------------------------------------------------------------------------------------------
# open() modes
# ------------------------------------------------------------------------------------------------------
# 'r', read, default mode, raises an error if file does not exist
# 'a', appending data, creates the file if it does not exist
# 'w', overwriting data
# 'x', create file, raises an error if file exists

with open("../support/demofile.txt", "a") as file:  # a parameter - appending data
    print("Appending data to demofile.txt")
    file.write("\nNow the file has more content.")


with open("../support/demofile.txt") as file:  # default r parameter - read mode
    print("\nReading appended data: ")
    print(file.read())


with open("../support/demofile.txt", "w") as file:  # w parameter - write mode
    print("overwriting demofile.txt")
    file.write("This is demofile.txt\nThis file is for testing purposes.\nThank you.")


with open("../support/demofile.txt") as file:  # default r parameter - read mode
    print("\nPrinting demofile.txt overwritten:")
    print(file.read())


with open("newFile.txt", "x") as file:  # x parameter - creating files
    print("Just creating a new file...")


# ------------------------------------------------------------------------------------------------------
# additional open() parameter
# ------------------------------------------------------------------------------------------------------
# 't', text, default
# 'b', binary, e.g. images


# ------------------------------------------------------------------------------------------------------
# deleting a file
# ------------------------------------------------------------------------------------------------------
import os

# before, check if file exists
if os.path.exists("newFile.txt"):
    os.remove("newFile.txt")
else:
    print("File does not exists.")


# deleting a folder
if os.path.exists("./newFolder"):
    os.rmdir("./newFolder")
else:
    print("Folder does not exists.")

