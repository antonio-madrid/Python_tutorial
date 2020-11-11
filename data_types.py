# Variables
# A regular variable declaration
globalVariable = "the way to declare a variable"

# 5 + ' number' error
# Python cannot add numbers to Strings

# ------------------------------------------------------------------------------------------------------

# Direct declaration
string = 'another way to declare a string'
integer = 1
aFloat = 2.2
complexNumber = 2j
aList = ["apple", "banana", "cherry"]
aTuple = ("apple", "banana", "cherry")  # tuple is an orderered and inmutable list
numberRange = range(5)
dicctionary = {"name": "Antonio", "age": 31}  # dicctionary is a hashtable, a JSON
aSet = {"apple", "banana", "cherry"}  # unordered and unindexed list
aFrozenSet = frozenset({"apple", "banana", "cherry"})
boolean = True
justBytes = b"bytes"
arrayBytes = bytearray(5)
aMemoryView = memoryview(bytes(5))

# ------------------------------------------------------------------------------------------------------

# Declare variables with constructors
integer = int(-10)
aFloat = float(2.3e3)  # e Exponential, power
complexNumber = complex(1j)  # j imaginary part
aList = list(("apple", "banana", "cherry"))
aTuple = tuple(("apple", "banana", "cherry"))
numberRange = range(6)
dicctionary = dict(name="Antonio", age=31)
aSet = set(("apple", "banana", "cherry"))
aFrozenSet = frozenset(("apple", "banana", "cherry"))
boolean = bool(0)
justBytes = bytes(5)
arrayBytes = bytearray(5)
aMemoryView = memoryview(bytes(5))
