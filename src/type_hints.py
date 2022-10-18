# New Python versions support type hints to add high level types to variables
# Python types are used as type checker and linter, it does not provide compilation type checking


# Basic types'
# str, int, float, bool
myString: str = 'Antonio'
myInteger: int = 33
myFloat: float = 1.2
myBoolean: bool = True


# Complex types
# complex, range, byte, bytearray, memoryview
myComplexNumber: complex = 2j
myNumberRange: range = range(10)
myBytes: bytes = bytes(6)
myArrayBytes: bytearray = bytearray(5)
myMemoryView: memoryview = memoryview(bytes(5))


# Collection types
# list, tuple, dict, set, frozenset
myList: list = ['apple', 'banana', 'cherry']
myTypedList: list[str] = ['apple', 'banana', 'cherry']

myTuple: tuple = ('apple', 'banana', 'cherry')
myTypedTuple: tuple[str, str, str] = ('apple', 'banana', 'cherry')

myDictionary: dict = {'name': 'Antonio', 'age': myInteger}
myTypedDictionary: dict[str:str] = {'name': 'Antonio', 'age': '${my}'}

mySet: set = {'apple', 'banana', 'cherry'}
myTypedSet: set[str] = {'apple', 'banana', 'cherry'}

myFrozenSet: frozenset = frozenset({'apple', 'banana', 'cherry'})
myTypedFrozenset: frozenset[str] = frozenset({'apple', 'banana', 'cherry'})


# Function types
# Input arguments and returned values can be typed

def greet(name: str) -> str:
    return 'Hello ' + name


print(greet(myString))


# Special primitives types


# Any type
# Python should import Any from typing
from typing import Any

# Any variables can store any type of value similar to TypeScript any
myAnyValueVariable: Any = 'String type'
print(f'myAnyValueVariable with a {type(myAnyValueVariable)} type: {myAnyValueVariable}')
myAnyValueVariable = 11  # number type
print(f'myAnyValueVariable with a {type(myAnyValueVariable)} type: {myAnyValueVariable}')
myAnyValueVariable = None  # void value
print(f'myAnyValueVariable with a {type(myAnyValueVariable)} (void) type: {myAnyValueVariable}')


# NoReturn
from typing import NoReturn


def noReturnFunction() -> NoReturn:
    print('This function should no return any value.')


noReturnFunction()


# TypeAlias
Factors = list[int]  # It allows to create alias of other types


# Special forms
# typing.Tuple
# typing.Union
# typing.Optional


from typing import Optional


def my_optional_function(optional: Optional[int] = None) -> None:
    if optional:
        print(optional)
    else:
        print('There is no optional argument.')


my_optional_function()


# Adding new types
# NewType allows to create new types

from typing import NewType

UserId = NewType('UserId', int)  # It defines the new type name and its type values
some_id = UserId(1234)
print(f'New UserId type: {UserId}')
print(f'New UserId type instance: {some_id}')

Person = NewType('Person', dict[str, str])  # it defines the Person type with a string dictionary inside it
manolo = Person({'name': 'Manolo', 'age': '45'})
print(f'New Person Type: {Person}')
print(f'New UserId type instance: {manolo}')


# type() function
# It checks variable types in Python

type(myList)  # it returns the myList variable type
print(f'myTypedList type is: {type(myTypedList)}')
