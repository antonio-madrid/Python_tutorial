# ------------------------------------------------------------------------------------------------------
# Lambdas
# ------------------------------------------------------------------------------------------------------

# No argument lamdas
lambda_without_args = lambda: print("No arguments lambda")
lambda_without_args()


# One argument lambdas
one_arg_lambda = lambda only_arg: print("Lambda with an only argument: " + only_arg)
one_arg_lambda("TheArgument")


# Multi-argument lamdas
my_lambda = lambda number_a, number_b: number_a * number_b
print(my_lambda(5, 5))
