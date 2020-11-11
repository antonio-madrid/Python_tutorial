# Classes

# ------------------------------------------------------------------------------------------------------

# A void class
class Void:
    pass


# ------------------------------------------------------------------------------------------------------

# Simple class
class MyClass:
    __privateAttribute__ = 0
    publicAttribute = "a public property"

    # Constructor
    def __init__(self, attribute2):
        # self = this
        # autoCreatedAttribute is create on the fly as a public one
        self.publicAutoCreatedAttribute = self.__stringify(attribute2)
        # __privateAutoCreatedAttribute is created on the fly as a private attribute
        self.__privateAutoCreatedAttribute = self.__stringify(attribute2 * 25)

    def set__attribute__(self, number):
        self.__privateAttribute__ = number

    def get__attribute__(self):
        return str(self.__privateAttribute__)

    # Auto created private properties starts with __
    def set__privateAutoCreatedAttribute(self, number):
        self.__privateAutoCreatedAttribute = int(number)

    # Private static method
    @staticmethod
    def __stringify(string):
        return str(string)


myObject = MyClass(2)
myObject.set__attribute__(1)
myObject.set__privateAutoCreatedAttribute(3)
print("Getting the private attribute: " + myObject.get__attribute__())
print("Directly getting the value of the publicAttribute: " + myObject.publicAttribute)
print("Getting the public autoCreatedAttribute: " + myObject.publicAutoCreatedAttribute)

# ------------------------------------------------------------------------------------------------------

# deleting a property
del myObject.publicAutoCreatedAttribute

# deleting an object
del myObject


# ------------------------------------------------------------------------------------------------------

class MyClassWithoutConstructor:
    attribute1 = 10

    def sum(self, number):
        return number + self.attribute1


withoutConstructor = MyClassWithoutConstructor()
print(withoutConstructor.sum(5))


# ------------------------------------------------------------------------------------------------------

# Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi, I am " + self.name + ', and I am ' + str(self.age) + " years old.")


antonio = Person("Antonio", 31)
antonio.greet()


class Student(Person):
    def __init__(self, name, age, graduation_year):
        super().__init__(name, age)
        self.__graduation_year = graduation_year

    def get_graduation_year(self):
        return self.__graduation_year


newStudent = Student("Antonio", 24, 2014)
newStudent.greet()
print("The graduation year of " + newStudent.name + " was: " + str(newStudent.get_graduation_year()))
