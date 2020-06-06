# String, Tuples, List, Dictionaries
# @ Michael

# Strings

s = "Hello Julia"
print(s[2])
print(s[:3])
print(s[:-3])
# l
# Hel
# Hello Ju

# Tuples
t1 = (1, 'two', 3)
t2 = (t1, 3.14)
print(t1+t2)
print((t1+t2)[2:5])
# (1, 'two', 3, (1, 'two', 3), 3.14)
# (3, (1, 'two', 3), 3.14)

# Both strings and tuples are not mutable

# This is very important!
# immutble: the objects of immutable types cannot be modified;
# mutable: the objects of mutable types can be modified

s[2] = 'u'  # you will get error
t1[2] = 6  # you will get error too


# List, which is mutable;
# List is a very important data type in Python, many high level datatype,
# such as matrix in numpy, and dataframe in panda
# Lists are extremely versatile and can be used to solve
# a variety of problems.

L = ['I did it all', 3, 'love', 5.8]
L[2]
L[1:4]

LL = [['MIT', 'Standord', 5], [4.6, 5.9, 3]]
len(LL)
LL[0]
LL[1][1]  # you should know you can put a list inside a list

# Dictionaries can be taken as `combined list`, which includes index and value

a = {'a': 1, 'b': 'hello', 'c': 5, 6: 7}
a[6]
a[2]  # you will get error as there is no index called 2
a['a']

# mutability of list
L[2] = 'evol'
L

# Know how to slice sequence (mainly focus on list)
ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ls[2:5]
ls[-3:]
ls[-3:-1]

# copy or slice ?

lsc = ls
lsc[1] = 'B'
print(ls)
print(lsc)
# ['a', 'B', 'c', 'd', 'e', 'f', 'g', 'h']
# ['a', 'B', 'c', 'd', 'e', 'f', 'g', 'h']

ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
lss = ls[:]
lss[1] = 'B'
print(ls)
print(lss)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# ['a', 'B', 'c', 'd', 'e', 'f', 'g', 'h']

# list might shrik
ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ls[2:7] = [56, 78, 19]
print(ls)  # ['a', 'b', 56, 78, 19, 'h']

# stride
ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ls[::2]


# sorted and starred expression
car_ages = [0, 13, 18, 7, 9, 21, 6]
car_ages_descending = sorted(car_ages, reverse=True)
oldes, second_oldest, *others = car_ages_descending  # starred expresion !
print(car_ages_descending)
print(oldes, second_oldest)
# [21, 18, 13, 9, 7, 6, 0]
# 21 18
#
