# Regular Expressions on Python
import re

text = "The rain in Spain"

# re.search() returns a Match object if there is a match
regex = re.search("^The.*Spain$", text)
print(regex)
print(regex.string)

# re.findAll() returns a list containing all matches
regex = re.findall("ai", text)
print(regex)

