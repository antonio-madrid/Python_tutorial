# To use modules, import them

# import keyword imports everything from miModule.py
from src.modules import miModule, miModule as miModuleAlias

# Using the module functions by full name
result = miModule.sum(5, 7)
print(result)

# Using the module variables by full name
print(miModule.moduleVariable)

# Using the module object by full name
print(miModule.moduleObject["name"])

# Renaming an imported module

print(miModuleAlias.sum(3, 3))

# Show all functions of a module
content = dir(miModuleAlias)
print(content)

# Import just an object, function or variable
from src.modules.miModule import moduleObject

print("age:")
print(moduleObject["age"])
