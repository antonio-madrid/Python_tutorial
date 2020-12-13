# main functions in Python

# Every Python script contains __name__ variable which indicates the name of the script
# When a Python script is directly executed by the Python interpreter, __name__ variable is set to __main__
# __main__ indicates a Python script is running as the main program

# if __name__ == "main"__: is used to prevent a block of code being run when a module is imported

print("__name__ variable value: " + __name__)

if __name__ == "__main__":
    print("Code executed as a Python script.")
else:
    print("Code executed as Python module")

