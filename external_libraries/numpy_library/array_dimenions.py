# ------------------------------------------------------------------------------------------------------
# Numpy
# ------------------------------------------------------------------------------------------------------

import numpy as np

# ------------------------------------------------------------------------------------------------------
# numpy version
# ------------------------------------------------------------------------------------------------------

# numpy.__version__ shows current NumPy version
print("NumPy version: " + np.__version__)


# ------------------------------------------------------------------------------------------------------
# Array object
# ------------------------------------------------------------------------------------------------------

# To create an array object, use numpy.array() function and pass it a list, tuple, or array-like object
ndarray = np.array([1, 2, 3, 4, 5])
print(ndarray)
print(type(ndarray))


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
print("Dimensions of the array: {}".format(array.ndim))
print("One dimension array: {}".format(array))

# Two dimensions, 2D array
# An array of arrays, every element of this array is 1D array
array = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
print("Dimensions of the array: {}".format(array.ndim))
print("Two dimension array:")
print(array)

# Three dimensions, 3D array
# An array of 2D arrays, multidimensional array
array = np.array(([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]))
print("Dimensions of the array: {}".format(array.ndim))
print("Three dimension array:")
print(array)


