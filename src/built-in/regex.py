# ------------------------------------------------------------------------------------------------------
# Regular Expressions on Python
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# General RegEx rules
# ------------------------------------------------------------------------------------------------------
#   [] 	    A set of characters 	                                                        "[a-m]"
#   \ 	    Signals a special sequence (can also be used to escape special characters)      "\d"
#   . 	    Any character (except newline character) 	                                    "he..o"
#   ^ 	    Starts with 	                                                                "^hello"
#   $ 	    Ends with 	                                                                    "planet$"
#   * 	    Zero or more occurrences 	                                                    "he.*o"
#   + 	    One or more occurrences 	                                                    "he.+o"
#   ? 	    Zero or one occurrence 	                                                        "he.?o"
#   {} 	    Exactly the specified number of occurrences 	                                "he.{2}o"
#   | 	    Either or 	                                                                    "falls|stays"
#   () 	    Capture and group

import re

text = "The rain in Spain"

# ------------------------------------------------------------------------------------------------------
# compile()
# ------------------------------------------------------------------------------------------------------
# Creates a RegEx pattern to be applied in any given string

pattern = re.compile("^The.*Spain$")  # creates a Pattern Object
matches = pattern.findall(text)  # Pattern object can be reused as many times as needed

print(f'findAll() by a Pattern object finds all the occurrences by the given RegEx: {matches}')


# ------------------------------------------------------------------------------------------------------
# re.search()
# ------------------------------------------------------------------------------------------------------
# returns a Match object with the first occurrence if found
# re.search(pattern, string)
matches = re.search("^The.*Spain$", text)

print(f'search() with "^The.*Spain$" RegEx has found a match: {matches}')
print(f'Original String where the RegEx was applied: {matches.string}')
print(f'Position of the first occurrence: {matches.start()}')
print(f'First occurrence value: {matches.group()}')


# if no matches, None is returned
matches = re.search("Portugal", text)
print(f'search() when no occurrences found, None is returned: matches = {matches}')


# ------------------------------------------------------------------------------------------------------
# findAll()
# ------------------------------------------------------------------------------------------------------
# returns a list containing all the occurrences

# re.findAll(pattern, string)
matches = re.findall("ai", text)
print(f'findAll() when finding occurrences: {matches}')


# if no matches, an empty list is returned
matches = re.findall("Portugal", text)
print(f'findAll() when not finding any occurrences: {matches}')


# ------------------------------------------------------------------------------------------------------
# split()
# ------------------------------------------------------------------------------------------------------
# returns a list where the string has been split at each match

# re.split(pattern, string)
matches = re.split('\\s', text)
print(f'split() when slicing a String by the given RegEx: {matches}')


# split(pattern, string, number_of_slices)
# third parameter can control the number of occurrences returned
matches = re.split('\\s', text, 1)
print(f'split() when controlling the number of slices returned: {matches}')


# ------------------------------------------------------------------------------------------------------
# sub()
# ------------------------------------------------------------------------------------------------------
# re.sub() substitutes the match with the given string

# sub(pattern, substitution_value, string)
matches = re.sub("\\s", "_", text)
print(f'sub() when substituting a string by the given RegEx: {matches}')


# ------------------------------------------------------------------------------------------------------
# RegEx flags in Python
# ------------------------------------------------------------------------------------------------------
# Flags allow to modify the RegEx behaviour
# GLOBAL flag is default in Python

#  Document here type of String
multiline_text = """The rain in Spain.
The rain in the UK.
The rain in Malaysia.
The rain in Spain.
The rain in SPAIN.
"""

# MULTILINE RegEx flag
# Allows to apply RegEx on multiline strings such as documents.
matches = re.search("^The.*Spain\\.$", multiline_text, re.MULTILINE)  # re.MULTILINE is the MULTILINE flag
if matches:
    print(f'Applying a search() with MULTILINE flag and returning the first occurrence {matches.group()}')


# IGNORECASE RegEx flag
# Ignores case-sensitive RegEx's default option
matches = re.findall("The.*Spain\\.", multiline_text, re.IGNORECASE)
if matches:
    print(f'Applying findAll() with IGNORECASE flag and returning all the occurrences {matches}')


# Using the parameter flags=
pattern = re.compile("The.*Spain\\.", flags=re.IGNORECASE)
matches = pattern.search(multiline_text)
if matches:
    print(f'Using flags= parameter: {matches.group()}')


# ------------------------------------------------------------------------------------------------------
# Using several RegEx flags
# ------------------------------------------------------------------------------------------------------

# Using + operator
matches = re.findall("^The.*Spain\\.$", multiline_text, flags=re.M + re.IGNORECASE)  # re.M is equal to re.MULTILINE
if matches:
    print(f'Applying a findAll() with MULTILINE & IGNORECASE flags and returing all the ocurrences: {matches}')


# Using | operator
matches = re.search("^The.*Spain\\.$", multiline_text, flags=re.M | re.I)  # re.I is equal to re.IGNORECASE
if matches:
    print(f'Applying search() with MULTILINE and IGONRECASE flags: {matches.group()}')  # returns first occurrence
