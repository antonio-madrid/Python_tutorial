# ------------------------------------------------------------------------------------------------------
# Shallow copies
# ------------------------------------------------------------------------------------------------------
# They are different objects with same values

person = {
    'name': 'Antonio',
    'age': 33
}


# ------------------------------------------------------------------------------------------------------
# Variable pointers
# ------------------------------------------------------------------------------------------------------
# Variables do not store objects, just point them

# other_person and person variables pointing to the same object
other_person = person  # they are storing the position of the same object


# ------------------------------------------------------------------------------------------------------
# copy()
# ------------------------------------------------------------------------------------------------------
# Python built-in method to create a shallow copy of an object

person_copy = person.copy()  # creates a new object with same values than the given one
person is person_copy  # False, their variables are pointing different objects
print(f'person and person_copy are different objects with same values. person is person_copy: {person is person_copy}')


# ------------------------------------------------------------------------------------------------------
# Equality Operator vs Identity Operator
# ------------------------------------------------------------------------------------------------------

# Equality operator checks every value of both objects are being equal
print(f'Equality operator: person == other_person: {person == other_person}')  # are the same values?
# Identity operator checks if both variables are pointing the same object
print(f'Identity operator: person is other_person: {person is other_person}')  # are the same object?


# ------------------------------------------------------------------------------------------------------
# Slice Operator [:]
# ------------------------------------------------------------------------------------------------------
# A simplified way to create a list Shallow Copy instead of using copy() function

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list_copied = my_list[:]  # They are different lists with the same values

print(f'Is my_list the same object than my_list_copied? : {my_list is my_list_copied}')

