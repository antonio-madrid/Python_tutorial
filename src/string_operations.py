# ------------------------------------------------------------------------------------------------------
# String types
# ------------------------------------------------------------------------------------------------------

# Simple string
string = "Hello world   "

# Multiline string
document_here = """
This is a text,
with several lines.
This allows to have a better reading.
This kind of string is name 'document here'
"""

# Raw string - r""
no_raw_string = 'Hello\nWorld'  # backslash allows to scape some characters by default
print('A normal string will use the \\ character to scape others.', '\nFor instance:')  # \n creates a new line
print('"Hello\\nWorld" = ', no_raw_string)
print('\\ will scape "n", creating a new line and ignoring \\')  # \\ allows to write \ as a character

raw_string = r'Hello\nWorld'  # Treats a string as a raw string, ignoring the scape characters \
print("r'' allows to use a string as a raw string, ignoring escaped characters without the need to do it manually.")
print(r"r'Hello\nWorld' = ", raw_string)  # r'' will display the \ characters instead of escaping others

# Raw strings are perfect for URLs or strings that use special character as such \
url_raw_string = r'https://www.wikipedia.org/'


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
