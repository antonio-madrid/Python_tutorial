# Classes

class MyClass:
    attribute = 1

    # Constructor
    def __init__(self, attribute):
        self.attribute = attribute


myObject = MyClass()
print(myObject.attribute)



# class Person:
#     def __init__(self, name, age):
#         self.name = "Antonio"
#         self.age = 31
#
#     def greet(self):
#         print("Hi, I am " + self.name + ', and I am ' + self.age + " years old.")
#
#
# antonio = Person("Antonio", 31)
# antonio.greet()