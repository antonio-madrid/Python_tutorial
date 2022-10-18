# ------------------------------------------------------------------------------------------------------
# Variables
# ------------------------------------------------------------------------------------------------------

# A regular variable declaration
globalVariable = "the way to declare a variable"

# 5 + ' number' error
# Python cannot add numbers to Strings


# ------------------------------------------------------------------------------------------------------
# Direct declaration
# ------------------------------------------------------------------------------------------------------

# Basic types
string_variable = 'another way to declare a string'
integer_variable = 1
float_variable = 2.2
boolean_variable = True


# Complex types
complex_number_variable = 2j
bytes_variable = bytes(5)
array_bytes_variable = bytearray(5)
memoryview_variable = memoryview(bytes(5))


# Collection types
list_variable = ["apple", "banana", "cherry"]  # ArrayList on Python
tuple_variable = ("apple", "banana", "cherry")  # tuple is an ordered and immutable list
number_range_variable = range(5)
dictionary_variable = {"name": "Antonio", "age": 31}  # dictionary is a hashtable, a JSON object
set_variable = {"apple", "banana", "cherry"}  # unordered and not indexed list
frozen_set_variable = frozenset({"apple", "banana", "cherry"})


# ------------------------------------------------------------------------------------------------------
# Declare variables with constructors
# ------------------------------------------------------------------------------------------------------

# Basic types
integer_variable = int(-10)
float_variable = float(2.3e3)  # e Exponential, power
boolean_variable = bool(0)


# Complex types
complex_number_variable = complex(1j)  # j imaginary part
bytes_variable = bytes(5)
array_bytes_variable = bytearray(5)
memoryview_variable = memoryview(bytes(5))


# Collection types
list_variable = list(("apple", "banana", "cherry"))
tuple_variable = tuple(("apple", "banana", "cherry"))
number_range_variable = range(6)
dictionary_variable = dict(name="Antonio", age=31)
set_variable = set(("apple", "banana", "cherry"))
frozen_set_variable = frozenset(("apple", "banana", "cherry"))
