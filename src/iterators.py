# ------------------------------------------------------------------------------------------------------
# Iterators
# ------------------------------------------------------------------------------------------------------

# Iterable objects (lists, tuples, dictionaries and sets)

myFruitTuple = ("banana", "apple", "peach")

# Iterator is an object that contains iterable objects
# and implements __next__() and __iter__()

myIterator = iter(myFruitTuple)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))


banaString = "banana"
myIterator = iter(banaString)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

# To create a new Iterator object
# Use the iter() constructor

numbers = [1, 2, 3, 4]
numerIter = iter(numbers)

# To iterate the iterator use build-in function next()

print(next(numerIter))
print(next(numerIter))
print(next(numerIter))


# ------------------------------------------------------------------------------------------------------
# Iterable classes
# ------------------------------------------------------------------------------------------------------

# To create an Iterable Class
# Implements __iter__() and __next__() functions

class IterableNumbers:
    # Initialize the iterator
    def __iter__(self):
        self.number = 0
        return self

    # Define the next operation
    def __next__(self):
        if self.number <= 5:
            number = self.number
            self.number += 1
            return number
        else:
            # StopIteration stops the iterator
            return StopIteration


iterableNumbers = IterableNumbers()
# iter() construct the iterator object from the iterator class
myIterNums = iter(iterableNumbers)

print("Showing iterableNumbers: ")
print(next(myIterNums))
print(next(myIterNums))
print(next(myIterNums))
print(next(myIterNums))
print(next(myIterNums))
print(next(myIterNums))
print(next(myIterNums))  # Doesn't iterate any longer
