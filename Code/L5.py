# First-Class Functions
# @ Michael

# Functions in Python are first-class objects. Programming language theorists
# define a “first-class object” as a program entity that can be:
# • Created at runtime
# • Assigned to a variable or element in a data structure
# • Passed as an argument to a function
# • Returned as the result of a function
# https://www.youtube.com/watch?v=kr0mpwqttM0

import random


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


class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
bingo.pick()
bingo()
callable(bingo)  # True


def logger(msg):

    def log_message():
        print('Log:', msg)

    return log_message


log_hi = logger('Hi')
log_hi()  # closure


def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


print_h1 = html_tag('h1')
print_h1('I Love Python')
print_h1('Data Scientist')
# <h1>I Love Python</h1>
# <h1>Data Scientist</h1>
# It's similiar to decerators

# Function Introspection
# at this stage, I would like you to look at the following table
# Name               Type                    Description
# __annotations__    dict           Parameter and return annotations
# __call__           method-wrapper Implementation of the () operator;
# __closure__        tuple           The function closure
# __code__           code   Function metadata and body compiled into bytecode
# __defaults__       tuple Default values for the formal parameters
# __get__  method-wrapper Implementation of the read-only descriptor protocol
# __globals__ dict Global variables of the module where the function is defined
# __kwdefaults__   dict Default values for the keyword-only formal parameters
# __name__         str The function name
# __qualname__     str The qualified function name
