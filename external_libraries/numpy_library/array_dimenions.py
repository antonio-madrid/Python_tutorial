# ------------------------------------------------------------------------------------------------------
# NumPy
# ------------------------------------------------------------------------------------------------------

import numpy as np

# ------------------------------------------------------------------------------------------------------
# NumPy version
# ------------------------------------------------------------------------------------------------------
# Library for managing fast multidimensional Arrays, arrays operations
# Also allows random number operations, statistical, basic linear algebra and discrete Fourier transforms
# NumPy operations are compiled in C and C++ for performance

# numpy.__version__ shows current NumPy version
print("NumPy version: " + np.__version__)

# ------------------------------------------------------------------------------------------------------
# ndarray = n-dimensional array = Array object
# ------------------------------------------------------------------------------------------------------
# ndarray = n-dimensional array = Array object

# To create an array object, use numpy.array() function and pass it a list, tuple, or array-like object
ndarray = np.array([1, 2, 3, 4, 5])
print(ndarray)
print(type(ndarray))

# ------------------------------------------------------------------------------------------------------
# NumPy arrays vs Python lists:
# ------------------------------------------------------------------------------------------------------
# NumPy arrays are constraint by C and C++ rules

# NumPy's arrays have fix size at creation
ndarray_fixed = np.array([1, 2, 3])
print(
    f'This is an ndarray with {ndarray_fixed.size} positions that cannot store more than {ndarray_fixed.size} values:')
print(ndarray_fixed)

# ndarray_fixed.append(4)  -  This operation is not possible
# The solution is creating a new array with the original values plus the new ones
new_ndarray_fixed = np.append(ndarray_fixed, [4, 5])
print(
    f'This is a new ndarray with {new_ndarray_fixed.size} positions '
    f'which stores the ndarray_fixed values and other two:'
)
print(new_ndarray_fixed)

# Original Python lists can increase their size on demand
python_mutable_list = [1, 2, 3]  # Original size is 3
print(f'Original Python list size: {len(python_mutable_list)}')
python_mutable_list.append(4)  # Adding values at the end of the list, increasing the size one position
python_mutable_list.append(5)

print(f'Python list size after adding to elements: {len(python_mutable_list)}')
print(python_mutable_list)

# All ndarray elements has to be the same data type, numbers, strings, objects, etc
ndarray_of_numbers = np.array([1, 2, 4])
ndarray_of_numbers[2] = 3  # Changing the third value for the same number type

# When assigning different data types to a NumPy array,
# Python will try to covert those values to the ndarray value types
ndarray_of_numbers[0] = '9'  # NumPy is going to convert the string number to a number to avoid errors
ndarray_of_numbers[0] = False  # NumPy is going to convert boolean values to 0 or 1 to avoid errors

# When Python cannot convert the given type to the ndarray type, it will throw an error
try:
    ndarray_of_numbers[0] = 'Antonio'
except ValueError:
    print('Python cannot convert a normal string to an Integer.')
try:
    ndarray_of_numbers[0] = {'name': 'Antonio'}
except TypeError:
    print('Python cannot convert a dictionary to an Integer.')

print(ndarray_of_numbers[2])

# ------------------------------------------------------------------------------------------------------
# Array dimensions
# ------------------------------------------------------------------------------------------------------

# Zero dimensions, 0D or scalars
# Arrays with an only one element
array = np.array(31)
# ndim property defines the array dimensions number
print("Dimensions of the array: {}".format(array.ndim))
print("Zero dimension array: {}".format(array))

# One dimension array, uni-dimensional array
# An array with a simple list of values, a normal array
array = np.array([31, 23, 18, 45, 34, 24])
print(f'Dimensions of the array: {array.ndim}')
print("One dimension array: {}".format(array))

# Two dimensions, 2D array
# An array of arrays, every element of this array is 1D array
array = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
print(f'Dimensions of the array: {array.ndim}')
print("Two dimension array:")
print(array)

# Three dimensions, 3D array
# An array of 2D arrays, multidimensional array
array = np.array(([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]))
print(f'Dimensions of the array: {array.ndim}')
print("Three dimension array:")
print(array)
