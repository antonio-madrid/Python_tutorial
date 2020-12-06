# Regular Expressions on Python
import re

text = "The rain in Spain"

# re.search() returns a Match object if there is a match
# re.search(pattern, string)
matches = re.search("^The.*Spain$", text)
print(matches)
print(matches.string)
print(matches.start())

# if no matches, None is returned
matches = re.search("Portugal", text)
print(matches)

# re.findAll() returns a list containing all matches
# re.findAll(pattern, string)
matches = re.findall("ai", text)
print(matches)

# if no matches, an empty list is returned
matches = re.findall("Portugal", text)
print(matches)

# re.split() returns a list where the string has been split at each match
matches = re.split('\s', text)
print(matches)

# third parameter can control the number of occurrences returned
matches = re.split('\s', text, 1)
print(matches)

# re.sub() replaces the matches with the given string
matches = re.sub("\s", "_", text)
print(matches)
