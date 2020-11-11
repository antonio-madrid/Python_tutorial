# Lambdas
lambdaWithoutArgs = lambda : print("No arguments lambda")
lambdaWithoutArgs()

oneArgLambda = lambda onlyArg : print("Lambda with an only argument: " + onlyArg)
oneArgLambda("TheArgument")

myLambda = lambda numberA, numberB : numberA * numberB
print(myLambda(5, 5))

