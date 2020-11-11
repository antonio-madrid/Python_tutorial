# Lambdas
lambda_without_args = lambda: print("No arguments lambda")
lambda_without_args()

one_arg_lambda = lambda only_arg: print("Lambda with an only argument: " + only_arg)
one_arg_lambda("TheArgument")

my_lambda = lambda numberA, numberB: numberA * numberB
print(my_lambda(5, 5))
