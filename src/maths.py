# Built-in Math functions

# min() returns the lowest value in an iterable
minimum = min(5, 2, 9, 7)
print("Minimum number of: 5, 2, 9, 7")
print(minimum)

# max() returns the highest value in an iterable
maximum = max(1, 5, 3, 7, 8, 0)
print("Maximum number of: 1, 5, 3, 7, 8")
print(maximum)

absolute = abs(-7.25)
print("Abolute positive value of 7.25")
print(absolute)

# pow() returns the value of x to the power of y
power = pow(4, 3) 
print("4 to the power of 3:") # 4 * 4 * 4
print(power)


# Built-in module math
import math

squareRoot = math.sqrt(64)
print("The square root of 64 is: ") # 8 * 8
print(squareRoot)

# math.ceil()
ceil = math.ceil(2.75)
print("2.75 rounded up")
print(ceil)

# math.floor()
floor = math.floor(2.75)
print("2.75 rounded down")
print(floor)

pi = math.pi
print("pi constant: ")
print(pi)

# How to get random numbers
# Using de built-in class random
import random
randomNumber = random.randrange(1, 10)

print("generated random number: ")
print(randomNumber)
