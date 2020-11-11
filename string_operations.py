# String operations

# slice an String, which are an array
string = "Hello world   "
print(string[0:5])

# .length in Python
len(string)

# removes whithespaces from the beginning or the end
print(string.strip() + '.')

# lower case
print(string.lower())

# upper case
print(string.upper())

# capitalize
print(string.capitalize())

# replace
print(string.replace("w", "W"))

# contains
print("ello" not in string)

# concatenate strings and numbers
string = "I am Antonio, and I am {}"
print(string.format(31))

# escaped character \
escapeCharacter = "\n"
