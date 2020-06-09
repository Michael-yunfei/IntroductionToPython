# Operator Overloading
# @ Michael
# Chapter 30

# Indexing and Slicing: __getitem__ and __setitem__
# __getitem__ and __setitem__ can custom the way of your datastructure


class Customlist:
    def __init__(self, elements=0):
        self.my_custom_list = [0] * elements

    def __setitem__(self, index, value):
        self.my_custom_list[index] = value

    def __getitem__(self, index):
        return 'Hey you are accessing {} element whose value is {}'.format(
            index, self.my_custom_list[index]
        )

    def __str__(self):
        return str(self.my_custom_list)


obj = Customlist(6)
obj[0] = 1
obj[2] = 8
print(obj[0])
print(obj[2])
print(obj)
# Hey you are accessing 0 element whose value is 1
# Hey you are accessing 2 element whose value is 8
# [1, 0, 8, 0, 0, 0]


# Building your own iterator: __iter__(), __next__()

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


a = PowTwo(4)
i = iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# 2
# 4
# 8
# 16
# StopIteration

for i in PowTwo(5):
    print(i)

# 1
# 2
# 4
# 8
# 16
# 32


# Attribute Reference

class Empty:
    def __getattribute__(self, attname):
        if attname == 'age':
            return 40
        else:
            raise AttributeError(attname)


empty_test = Empty()
empty_test.age
empty_test.name


class acesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'gender':
            self.__dict__[attr] = value % 2
        else:
            raise AttributeError(attr + ' not allowed')


a = acesscontrol()
a.gender = 10
a.gender
a.gender = 11
a.gender

# String Representation: __repr__ and __str__
# Read this: https://github.com/Michael-yunfei/magicmethods
