# First-Class Functions
# @ Michael

# Functions in Python are first-class objects. Programming language theorists
# define a “first-class object” as a program entity that can be:
# • Created at runtime
# • Assigned to a variable or element in a data structure
# • Passed as an argument to a function
# • Returned as the result of a function


# First function example
def fanctorial(n):
    ''''Return n!'''
    return 1 if n < 2 else n*fanctorial(n-1)


print(fanctorial(18))
fanctorial.__doc__
type(fanctorial)

# 6402373705728000
# "'Return n!"
# function

print(list(map(fanctorial, range(9))))

# Higher order function
# A function that takes a function as argument or returns a function
# as the result is a higher-order function.

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits))
print(sorted(fruits, key=len))
# ['apple', 'banana', 'cherry', 'fig', 'raspberry', 'strawberry']
# ['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']


def reverse(words):
    return words[::-1]


reverse('hello')

print(sorted(fruits, key=reverse))
# ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']

# In the functional programming paradigm, some of the best known
# higher-order functions are map, filter, reduce, and apply.
# The apply function was deprecated in Python 2.3 and removed
# in Python 3 because it’s no longer necessary.

# The map and filter functions are still built-ins in Python 3,
# but since the introduction of list comprehensions and generator expressions,
# they are not as important.

# User-Defined Callable Types



















#
