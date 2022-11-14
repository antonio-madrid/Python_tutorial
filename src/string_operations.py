string = "Hello world   "

document_here = """
This is a text,
with several lines.
This allows to have a better reading.
This kind of string is name 'document here'
"""

# ------------------------------------------------------------------------------------------------------
# String interpolation
# ------------------------------------------------------------------------------------------------------
# It allows inserting variables’ or expression values into a String.

# It uses the string function f''
stringInterpolated = f'This is the value of string variable: {string}'
print(stringInterpolated)

import datetime

fullDateTime = datetime.datetime.now()

print(f"This is another String Interpolation, and today's date is {fullDateTime}")


# ------------------------------------------------------------------------------------------------------
# Standard operations
# ------------------------------------------------------------------------------------------------------

# slice a String, which are an array
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
