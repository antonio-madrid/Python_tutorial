# To use modules, import them

# import imports everything from modules.py
import modules

# Using the module functions by full name
result = modules.sum(5, 7)
print(result)

# Using the module variables by full name
print(modules.moduleVariable)

# Using the module object by full name
print(modules.moduleObject["name"])

# Renaming an imported module
import modules as miModule

print(miModule.sum(3, 3))

# Show all functions of a module
content = dir(miModule)
print(content)

# Import just an object, function or variable
from modules import moduleObject

print("age:")
print(moduleObject["age"])
