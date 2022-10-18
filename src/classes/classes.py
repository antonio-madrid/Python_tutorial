# ------------------------------------------------------------------------------------------------------
# A void class
# ------------------------------------------------------------------------------------------------------
class Void:
    pass


# ------------------------------------------------------------------------------------------------------
# Simple class
# ------------------------------------------------------------------------------------------------------
class MyClass:
    # ------------------------------------------------------------------------------------------------------
    # Class attributes
    # ------------------------------------------------------------------------------------------------------
    __private_attribute__ = 0
    public_attribute = "a public property"

    # ------------------------------------------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------------------------------------------
    def __init__(self, attribute2):
        # self = this
        # autoCreatedAttribute is created on the fly as a public one
        self.public_auto_created_attribute = self.__stringify(attribute2)
        # __privateAutoCreatedAttribute is created on the fly as a private attribute
        self.__private_auto_created_attribute = self.__stringify(attribute2 * 25)

    # ------------------------------------------------------------------------------------------------------
    # Class methods
    # ------------------------------------------------------------------------------------------------------
    # Setter
    def set__private_attribute__(self, number):
        self.__private_attribute__ = number

    # Getter
    def get__private_attribute__(self):
        return str(self.__private_attribute__)

    # Auto created private properties starts with __
    def set__private_auto_created_attribute(self, number):
        self.__private_auto_created_attribute = int(number)

    # Private static method
    @staticmethod
    def __stringify(string):
        return str(string)


# ------------------------------------------------------------------------------------------------------
# Simple class operations
# ------------------------------------------------------------------------------------------------------

myObject = MyClass(2)
myObject.set__private_attribute__(1)
myObject.set__private_auto_created_attribute(3)
print("Getting the private attribute: " + myObject.get__private_attribute__())
print("Directly getting the value of the publicAttribute: " + myObject.public_attribute)
print("Getting the public autoCreatedAttribute: " + myObject.public_auto_created_attribute)


# ------------------------------------------------------------------------------------------------------
# Delete operations
# ------------------------------------------------------------------------------------------------------

# deleting an object property
del myObject.public_auto_created_attribute

# deleting an object
del myObject


# ------------------------------------------------------------------------------------------------------
# No constructor class
# ------------------------------------------------------------------------------------------------------

class MyClassWithoutConstructor:
    attribute1 = 10

    def sum(self, number):
        return number + self.attribute1


# ------------------------------------------------------------------------------------------------------
# No constructor class operations
# ------------------------------------------------------------------------------------------------------

withoutConstructor = MyClassWithoutConstructor()
print(withoutConstructor.sum(5))


# ------------------------------------------------------------------------------------------------------
# Class inheritance
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# Parent class
# ------------------------------------------------------------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi, I am " + self.name + ', and I am ' + str(self.age) + " years old.")


# ------------------------------------------------------------------------------------------------------
# Parent class operations
# ------------------------------------------------------------------------------------------------------
antonio = Person("Antonio", 31)
antonio.greet()


# ------------------------------------------------------------------------------------------------------
# Child class or subclass
# ------------------------------------------------------------------------------------------------------
class Student(Person):
    def __init__(self, name, age, graduation_year):
        super().__init__(name, age)
        self.__graduation_year = graduation_year

    def get_graduation_year(self):
        return self.__graduation_year


# ------------------------------------------------------------------------------------------------------
# Child class or subclass operations
# ------------------------------------------------------------------------------------------------------
newStudent = Student("Antonio", 24, 2014)
newStudent.greet()
print("The graduation year of " + newStudent.name + " was: " + str(newStudent.get_graduation_year()))
