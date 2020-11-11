# Functions

globalVariable = "the way to declare a variable"


def my_function():
    # to change a global variable value use keyword global
    global globalVariable
    globalVariable = 'other way to declare a string'

    return 0


my_function()


def my_function_with_args(first_arg, second_arg):
    print(first_arg + ' ' + second_arg)


my_function_with_args("hello", 'there')


# Function with unknown list or args passed by a tuple
def unknown_multi_args(*tuple_of_args):
    print(tuple_of_args[0])


unknown_multi_args("could be one ", "two", "or unlimited")


# Function with unknown list or args passed by a dictionary
def unknown_multi_args(**kwargs):
    print("This is a dictionary, kwargs['name']: ")
    print(kwargs["name"])


unknown_multi_args(name="Antonio")


def function_with_default_param(country="Spain"):
    print('I am from ' + country)


function_with_default_param("UK")
function_with_default_param()


# pass keyword let's leave a function or a if statement void
def my_function():
    pass
