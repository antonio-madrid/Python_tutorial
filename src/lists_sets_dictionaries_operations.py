# ------------------------------------------------------------------------------------------------------
# Lists
# ------------------------------------------------------------------------------------------------------
# Python does not have built-in support for Arrays, use lists instead

my_list = list(("apple", "banana", "cherry"))
my_dictionary = {"name": "Antonio", "age": 31}  # dictionary is a hashtable, a JSON

# Range in a list
print(my_list[1:3])

# take a value
print(my_list[0])

# Loop through a List
for fruit in my_list:
    print(fruit)

# check if an item exists
print("banana" in my_list)

# Add items
my_list.append("mango")
my_list.append("orange")
my_list.append("strawberry")

fruitList = my_list

# Remove items
my_list.remove("mango")  # Deletes a specific item by the given value
my_list.pop()  # Deletes the last item
del my_list[3]  # Deletes a specific item by the given position
my_list.clear()  # Deletes all the collection values


# ------------------------------------------------------------------------------------------------------
# Sets
# ------------------------------------------------------------------------------------------------------
# Sets has the similar methods


# ------------------------------------------------------------------------------------------------------
# Dictionary
# ------------------------------------------------------------------------------------------------------

# Get a value by its key
my_dictionary["name"] = "Antonio"
my_dictionary.get("age")

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
