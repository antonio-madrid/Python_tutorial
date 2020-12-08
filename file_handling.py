# with open is a shortcut of open(), avoiding the use of try block and .close() function

# open() modes
# 'r', read, default mode, raises an error if file does not exist
# 'a', appending data, creates the file if does not exist
# 'w', writing data
# 'x', create file, raises an error if file exists

# additional open() parameter
# 't', text, default
# 'b', binary, e.g. images

# open() must to be in a try block and also need to be closed
try:
    f = open("./demofile.txt")  # 'rt' as a second parameter by default
    data = f.read()
    print(data)
    f.close()
except IOError:
    print("Cannot open the file")

# with open() is a sugar sintax, avoiding the use of try block and close() function
# file must to be specify with an alias
with open("demofile.txt") as file:
    partial_data = file.read(5)
    print("printing partial data")
    print(partial_data)

