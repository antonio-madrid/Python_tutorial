import json

# Stringify JSON
someJSON = '{"name": "Antonio", "age": 30, "city": "Malaga"}'

# json.loads() parse JSON string to a dictionary
parsedJSON = json.loads(someJSON)

print("printing JSON property 'age': ")
print(parsedJSON["age"])

# Creating an object similar to JSON object
dictionary = {
    "name": "Raul",
    "lastName": "Montoya",
    "city": "Malaga"
}

# json.dumps() parse a Python data type to a JSON string
jsonObject = json.dumps(dictionary)

print("printing a JSON string: ")
print(jsonObject)

# Every Python data type is parsed to a JavaScript data type

jsonNumber = json.dumps(8)
print("printing a JSON number from Python: ")
print(jsonNumber)

jsonNull = json.dumps(None)
print("printing a JSON null value from Python: ")
print(jsonNull)

jsonArray = json.dumps(["apple", "banana"])
print("printing a JSON array from a Python list: ")
print(jsonArray)

jsonArray = json.dumps(("mangos", "avocados"))
print("printing a JSON array from a Python tuple: ")
print(jsonArray)

allPythonTypes = {
    "name": "Antonio",
    "age": 31,
    "married": True,
    "divorced": False,
    "children": ("Nadia", "Arturo"),
    "pets": None,
    "vehicles": [
        {"model": "Marauder 250", "age": 9},
        {"model": "Altea XL", "age": 12}
    ]
}

# indent= parameter formats JSON strings in a readable way
print(json.dumps(allPythonTypes, indent=2))
