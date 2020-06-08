# Class: a realistic example
# @ Michael
# Learning Python: chapter 28

# Specifically, in this chapter we’re going to code two classes:
# • Person—a class that creates and processes information about people
# • Manager—a customization of Person that modifies inherited behavior


class person:
    def __init__(self, name, jobs, age, pay):
        self.name = name
        self.jobs = jobs
        self.age = age
        self.pay = pay


# we can set dafault value
class Person:
    def __init__(self, name, jobs, age=None, pay=0):
        self.name = name
        self.jobs = jobs
        self.age = age
        self.pay = pay


# Testing class
bob = Person('Bob Dylan', 'Musician')
sue = Person('Sue Jones', 'Laywer', 36, 10000)
print(bob.name, sue.pay)


# wrap the test for engineers and don't show it for customers
class PersonF:
    def __init__(self, name, jobs, age=None, pay=0):
        self.name = name
        self.jobs = jobs
        self.age = age
        self.pay = pay


if __name__ == '__main__':
    # self test code
    bob = PersonF('Bob Dylan', 'Musician')
    sue = PersonF('Sue Jones', 'Laywer', 36, 10000)
    print(bob.name, sue.pay)


# Step 2: Adding Behavior Methods
if __name__ == '__main__':
    # self test code
    bob = PersonF('Bob Dylan', 'Musician')
    sue = PersonF('Sue Jones', 'Laywer', 36, 10000)
    print(bob.name, sue.pay)
    print(bob.name.split()[-1])
    sue.pay *= 1.20
    print('%.2f' % sue.pay)


# encapsulation: wrapping up operation logic behind interfaces,
# such that each operation is coded only once in our program.


class personEn:
    def __init__(self, name, jobs, age=None, pay=0):
        self.name = name
        self.jobs = jobs
        self.age = age
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1+percent))


if __name__ == '__main__':
    # self test code
    bob = personEn('Bob Dylan', 'Musician')
    sue = personEn('Sue Jones', 'Laywer', 36, 10000)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(0.1)
    print(sue.pay)

# Dylan Jones
# 11000


# Providing Print Displays

class personEn:
    def __init__(self, name, jobs, age=None, pay=0):
        self.name = name
        self.jobs = jobs
        self.age = age
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1+percent))

    def __repr__(self):
        return '[Person: {}, {}]'.format(self.name, self.pay)


if __name__ == '__main__':
    # self test code
    bob = personEn('Bob Dylan', 'Musician')
    sue = personEn('Sue Jones', 'Laywer', 36, 10000)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(0.1)
    print(sue.pay)
    print(sue)


# Coding Subclasses

class Manger(personEn):
    def giveRaise(self, percent, bonus=0.1):
        personEn.giveRaise(self, percent+bonus)  # good way of coding


if __name__ == '__main__':
    # self test code
    bob = personEn('Bob Dylan', 'Musician')
    sue = personEn('Sue Jones', 'Laywer', 36, 10000)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(0.1)
    print(sue.pay)
    print(sue)
    tom = Manger('Tom Gutta', 'manager', '51', 50000)
    tom.giveRaise(0.1)
    print(tom)


# in OOP, we program by customizing what has already been done,
# rather than copying or changing existing code

# Customizing Constructors, Too

class Manger(personEn):
    def __init__(self, name, pay):
        personEn.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=0.1):
        personEn.giveRaise(self, percent+bonus)


# In this complete form, and despite their relatively small sizes,
# our classes capture nearly all the important concepts in OOP machinery:
# • Instance creation—filling out instance attributes
# • Behavior methods—encapsulating logic in a class’s methods
# • Operator overloading—providing behavior for built-in operations (printing)
# • Customizing behavior—redefining methods in subclasses to specialize them
# • Customizing constructors—adding initialization logic to superclass steps

# SUMMARY: instance, behavior, operator

# Using Introspection Tools

print(bob)
print(bob.__class__)
print(bob.__class__.__name__)
list(bob.__dict__.keys())
# [Person: Bob Dylan, 0]
# <class '__main__.personEn'>
# personEn
# ['name', 'jobs', 'age', 'pay']
