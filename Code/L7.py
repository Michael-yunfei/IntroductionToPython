# Class Coding Basic
# @ Michael

# Classes Generate Multiple Instance Objects
# I like using classes a lot as it works efficiently
# Classes are very like a manufactory which do things systematically
# You always need a self !


# A very simple example
class seClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


x1 = seClass()  # initialize a class
x2 = seClass()  # second one
print(x1)
x1.setdata('New')
x2.setdata(3.1415926)
x1.display()
x2.display()
# New
# 3.1415926

# Think of Class as a tool/manufactory that you can use repeatedly


# Inherits
class Inclass(seClass):
    def display(self):
        print('Current value = "%s"' % self.data)


z = Inclass()
z.setdata(42)
z.display()
print(z)
# Inheritance is more like updated version of first class

# Classes Can Intercept Python Operators
# Attributes


class Atclass(Inclass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return Atclass(self.data+other)

    def __str__(self):
        return '[ThirdClass: %s]' % self.data

    def mul(self, other):  # be aware of difference between this one and above
        self.data *= other


a = Atclass('abc')
a.display()  # inherited from Inclass
print(a)  # compare with print(z), this type we added string attribute
# [ThirdClass: abc]
b = a + 'xyz'
b.display()
print(b)
# [ThirdClass: abcxyz]

# b automatically becomes a CLASS!
# This is very important!

a.mul(3)
print(a)


class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age

    def info(self):
        return(self.name, self.jobs)


p1 = Person('Michael', 'Data Scientist', 32)
p2 = Person('Emmnet', 'Economist', 28)
print(p1)
p1.info()
p2.info()
#
