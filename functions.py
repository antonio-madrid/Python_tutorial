# Functions

globalVariable = "the way to declare a variable"

def myFunction():
    # to change a global variable value use keyword global
    global globalVariable
    globalVariable = 'other way to declare a string'

    return 0


myFunction()

def myFunctionWithArgs(firstArg, secondArg):
    print(firstArg + ' ' + secondArg)


myFunctionWithArgs("hello", 'there')

# Function with unknown list or args passed by a tuple
def unknownMultiArgs(*tupleOfArgs):
    print(tupleOfArgs[0])


unknownMultiArgs("could be one ", "two", "or unlimited")

# Function with unknown list or args passed by a dictionary
def unknownMultiArgs(**kwargs):
    print("This is a dictionary, kwargs['name']: ")
    print(kwargs["name"])


unknownMultiArgs(name="Antonio")


def functionWithDefaultParam(country="Spain"):
    print('I am from ' + country)


functionWithDefaultParam("UK")
functionWithDefaultParam()


# pass keyword let's leave a function or a if statement void
def myFunction():
    pass

