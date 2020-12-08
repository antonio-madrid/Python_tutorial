# with open is a shortcut of open(), avoiding the use of try block and .close() function

# open() modes
# 'r', read, default mode, raises an error if file does not exist
# 'a', appending data, creates the file if does not exist
# 'w', overwriting data
# 'x', create file, raises an error if file exists

# additional open() parameter
# 't', text, default
# 'b', binary, e.g. images

# open() must to be in a try block and also need to be closed
try:
    f = open("./demofile.txt")  # 'rt' as a second parameter by default
    # read() loads all data in a file
    data = f.read()
    print("Printing all the data in a try block:")
    print(data)
    f.close()
except IOError:
    print("Cannot open the file")

# with open() is a sugar sintax, avoiding the use of try block and close() function
# file must to be specify with an alias
with open("demofile.txt") as file:
    partial_data = file.read(5)
    print("Printing partial data")
    print(partial_data)

    # readline() allows to load a full line
    print("printing lines:")
    print(file.readline())
    print(file.readline())


with open("demofile.txt", "a") as file:
    print("Appending data to demofile.txt")
    file.write("\nNow the file has more content.")


with open("demofile.txt") as file:
    print("\nReading appended data: ")
    print(file.read())


with open("demofile.txt", "w") as file:
    print("overwriting demofile.txt")
    file.write("This is demofile.txt\nThis file is for testing purposes.\nThank you.")


with open("demofile.txt") as file:
    print("\nPrinting demofile.txt overwritten:")
    print(file.read())


with open("newFile.txt", "x") as file:
    print("Just creating a new file...")


# deleting a file
import os

# before, checking  if file exists
if os.path.exists("newFile.txt"):
    os.remove("newFile.txt")
else:
    print("File does not exists.")


# deleting a folder
if os.path.exists("./newFolder"):
    os.rmdir("./newFolder")
else:
    print("Folder does not exists.")

