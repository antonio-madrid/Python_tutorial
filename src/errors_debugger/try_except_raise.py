# ------------------------------------------------------------------------------------------------------
# try / except
# ------------------------------------------------------------------------------------------------------

# Standard try / except block
try:
    print("try block allows to run code with a risk of throwing errors")
except:
    print("except block allows exception handling")
else:
    print("Else block allows to execute code when nothing went wrong")
finally:
    print("finally block allows to execute code, regardless the result of a try/except blocks")


# Multiple exceptions try / except block
try:
    print("multiple exceptions handling")
except NameError:
    print("NameError exception caught")
except:
    print("General exception caught")


# ------------------------------------------------------------------------------------------------------
# Raise exceptions
# ------------------------------------------------------------------------------------------------------

# To throw an Exception, use raise
try:
    raise ArithmeticError("Arithmetic error thrown")
except ArithmeticError:
    print("Arithmetic error caught")

try:
    string = "string"
    if not type(string) in int:
        raise TypeError("Only integers allowed")
except TypeError:
    print("TypeError exception caught")



