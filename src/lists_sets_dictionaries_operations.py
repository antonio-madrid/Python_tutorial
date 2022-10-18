# ------------------------------------------------------------------------------------------------------
# Lists
# ------------------------------------------------------------------------------------------------------
# Python does not have built-in support for Arrays, use lists instead

aList = list(("apple", "banana", "cherry"))
dicctionary = {"name": "Antonio", "age": 31}  # dicctionary is a hashtable, a JSON

# Range in a list
print(aList[1:3])

# take a value
print(aList[0])

# Loop through a List
for fruit in aList:
    print(fruit)

# check if item exists
print("banana" in aList)

# Add items
aList.append("mango")
aList.append("orange")
aList.append("strawberry")

fruitList = aList

# Remove items
aList.remove("mango")
aList.pop()
del aList[3]
aList.clear()


# ------------------------------------------------------------------------------------------------------
# Sets
# ------------------------------------------------------------------------------------------------------
# Sets has the similar methods


# ------------------------------------------------------------------------------------------------------
# Dictionary
# ------------------------------------------------------------------------------------------------------

# Get a value
dicctionary["name"] = "Antonio"
dicctionary.get("age")

# nested dictionaries
myFamily = {
    "mom": {
        "name": "Antonia",
        "age": 60
    },
    "dad": {
        "name": "Jose",
        "age": 60
    },
    "sister": {
        "name": "Isa",
        "age": 35
    }
}
