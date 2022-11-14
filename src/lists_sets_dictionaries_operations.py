# ------------------------------------------------------------------------------------------------------
# Lists
# ------------------------------------------------------------------------------------------------------
# Python does not have built-in support for Arrays, use lists instead

my_list = list(("apple", "banana", "cherry"))

# Takes a value
print(my_list[0])

# Loops through a List
for fruit in my_list:
    print(fruit)

# Checks if an item exists
print("banana" in my_list)

# Adds items
my_list.append("mango")
my_list.append("orange")
my_list.append("strawberry")

# Creates a new list which is a copy of my_list
fruitList = my_list.copy()  # Creates a Shallow Copy of my_list

# Removes items
my_list.remove("mango")  # Deletes a specific item by the given value
my_list.pop()  # Deletes the last item
del my_list[3]  # Deletes a specific item by the given position
my_list.clear()  # Deletes all the collection values

# ------------------------------------------------------------------------------------------------------
# slice()
# ------------------------------------------------------------------------------------------------------
# Specifies how to slice a sequence
# slice() it is not inclusive, it does not include the end position value

my_num_list = [0, 1, 2, 3, 4, 5, 6]
print(f'my_num_list = {my_num_list}')

# slice(stop_position)
my_slice = slice(2)  # it slices any list taking the given numbers
my_num_list_sliced = my_num_list[my_slice]  # Only contains first two elements of my_num_list
print(f'my_num_list with slice(2) = {my_num_list_sliced}')

# slice(start_position, end_position)
my_slice = slice(3, 5)  # It slices from position 3 until position 5, it does not include position 5 value
my_num_list_sliced = my_num_list[my_slice]  # Only contains two elements, from position 3 to 5
print(f'my_num_list with slice(3, 5) = {my_num_list_sliced}')

# slice(start_position, end_position, step)
my_slice = slice(1, 6, 2)  # It slices from position 1 until position 6, stepping 2, not including position 6 value
my_num_list_sliced = my_num_list[my_slice]  # Only contains three elements, from position 1 to 6
print(f'my_num_list with slice(1, 6, 2) = {my_num_list_sliced}')


# ------------------------------------------------------------------------------------------------------
# Slice Operator [:]
# ------------------------------------------------------------------------------------------------------
# It is sugar syntax to apply the slice() function


my_num_list_sliced = my_num_list[2:]  # Starts the slicing from position 2, not including position 2 value which is 1
print(f'my_num_list with [2:] = {my_num_list_sliced}')  # It returns all the elements starting from position 2

my_num_list_sliced = my_num_list[:2]  # Similar to slice(2), taking just 2 elements starting from the beginning
print(f'my_num_list with [:2] = {my_num_list_sliced}')  # It returns all the given elements, 2 in this case

my_num_list_sliced = my_num_list[1:6:2]  # Similar to slice(1, 6, 2)
print(f'my_num_list with [1:6:2] = {my_num_list_sliced}')  # It slices from position 1 until position 6, stepping 2

my_num_list_sliced = my_num_list[::3]  # It slices the list stepping 3
print(f'my_num_list with [::3] = {my_num_list_sliced}')  # Only contains the elements which positions are divisible by 3

my_num_list_sliced = my_num_list[:]  # Creates a Shallow Copy of the list as copy() function does
print(f'my_num_list with [:] = {my_num_list_sliced}')  # Only contains the elements which positions are divisible by 3


# ------------------------------------------------------------------------------------------------------
# Sets
# ------------------------------------------------------------------------------------------------------
# Sets has the similar methods


# ------------------------------------------------------------------------------------------------------
# Dictionary
# ------------------------------------------------------------------------------------------------------
my_dictionary = {"name": "antonio", "age": 31}  # dictionary is a hashtable, a JSON

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
