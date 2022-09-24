import datetime

fullDateTime = datetime.datetime.now()
print(fullDateTime)

# datetime contains several methods and variables to manipulate dates
year = fullDateTime.year
print(year)

# Create a new DateTime
birthdate = datetime.datetime(1989, 6, 27)
print(birthdate)

# Formatting a date into a readable string
month = fullDateTime.strftime("%B")
print(month)

# strftime string format time within a given code
formattedDate = fullDateTime.strftime("%B %d of %Y")
print(formattedDate)
