try:
    print("try block allows to run code with a risk of throwing errors")
except:
    print("except block allows exception handling")
else:
    print("Else block allows to execute code when nothing went wrong")
finally:
    print("finally block allows to execute code, regardless the result of a try/except blocks")


try:
    print("multiple exceptions handling")
except NameError:
    print("NameError exception caught")
except:
    print("General exception caught")


