# String Methods, numpy array, and zip function
# @ Michael

# there are many string methods, we will just introduce some of them

import string
import numpy as np

text = 'The value of pi is '
pi = 3.14
print(text + str(pi))

# count
text.count('i')  # 2
text.upper()

string.punctuation

text.split()  # return a list
'+@+'.join(['a', 'b', 'c'])

text.replace('pi', 'exponential')

text + 'haha'


# String methods are very important for people who want to do web scraping
# you might build up your skills later when you do more tasks on web scraping


# Array
# An array is a data structure that stores values of SAME DATA TYPE.
# In Python, this is the main difference between arrays and lists.

vector = np.arange(10)
print(vector)
print(vector * 2)
# [0 1 2 3 4 5 6 7 8 9]
# [ 0  2  4  6  8 10 12 14 16 18]

vector.reshape((2, 5))
print(np.zeros((6, 6)))
# [[0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0.]]


# Zip function
# Returns an iterator of tuples, where the i-th tuple contains
# the i-th element from each of the argument sequences or iterables.
# The iterator stops when the shortest input iterable is exhausted.

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zip(numbers, letters)
type(zip(numbers, letters))
print(list(zip(numbers, letters)))
print(list(zip(letters, numbers)))
# [(1, 'a'), (2, 'b'), (3, 'c')]
# [('a', 1), ('b', 2), ('c', 3)]
# IT RUTURNS AN ITERATOR OF TUPLES

for i, l in zip(numbers, letters):
    print(f'Letters: {l}')
    print(f'Numbers: {i}')

# Letters: a
# Numbers: 1
# Letters: b
# Numbers: 2
# Letters: c
# Numbers: 3

# building dictionaries

field = ['names', 'last_name', 'age', 'job']
values = ['Emmet', 'Heather', '28', 'Data Scientist']

a_dict = dict(zip(field, values))

# Learn more from this website:
# https://realpython.com/python-zip-function/

# Differences between pass, continue and break

for i in range(5):
    if i == 3:
        pass
    print(i)

# 0
# 1
# 2
# 3
# 4


for i in range(5):
    if i == 3:
        continue
    print(i)

# 0
# 1
# 2
# 4


for i in range(5):
    if i == 3:
        break
    print(i)

# 0
# 1
# 2

# Comprehensions
