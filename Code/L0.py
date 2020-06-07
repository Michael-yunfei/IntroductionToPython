# Python Thinking
# @ Michael

# Python aims at maximizing readability
# In terminal, check your python version: python --version


# Know the difference between bytes and str
a = b'h\x65llo'
print(list(a))
print(a)
# [104, 101, 108, 108, 111]
# b'hello'

a = 'a\u0300 propos'
print(list(a))
print(a)
# ['a', '̀', ' ', 'p', 'r', 'o', 'p', 'o', 's']
# à propos


# Convert bytes to string
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str


print(repr(to_str(b'foo')))
print(repr(to_str('bar')))
# 'foo'
# 'bar'


# Convert string to bytes
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of bytes


print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))
# b'foo'
# b'bar'

# % operator
print(b'red %s' % b'blue')
print('red %s' % 'blue')
print(b'red %s' % 'blue')

# bytes contains sequences of 8-bit values,
# and str contains sequences of Unicode code points.


# Print Format

# modulo operator %

print("Total Students: %1d, Boys: %1d" % (260, 139))
print("Total Students: %5d, Boys: %1d" % (260, 139))
# Total Students: 260, Boys: 139
# Total Students:   260, Boys: 139

# String.format method
# https://realpython.com/python-formatted-output/

# Important!
# Prefer enumerate over range
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print(f'{flavor} is delicious')


for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i+1}: {flavor}')


# 1: vanilla
# 2: chocolate
# 3: pecan
# 4: strawberry


# enumerate yields pairs of the loop index
# and the next value from the given iterator.
for i, flavor in enumerate(flavor_list):
    print(f'{i+1}: {flavor}')

# Specify the beginning counting number
for i, flavor in enumerate(flavor_list, 1):
    print(f'{i}: {flavor}')

# Prefer enumerate instead of looping over a range and indexing into a sequence
#  You can supply a second parameter to enumerate to specify the number
# from which to begin counting (zero is the default).


# Use zip to Process Iterators in Parallel

names = ['Michael', 'Julia', 'Emment']
counts = [len(n) for n in names]
print(counts)

# find the longest name
longest_name = None
max_count = 0
for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)


# zip wraps two or more iterators with a lazy generator
# The zip generator yields tuples containing the next value from each iterator

for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)


#  zip truncates its output silently to the shortest iterator
# if you supply it with iterators of different lengths.
# Use the zip_longest function from the itertools
# builtin module if you want to use zip on iterators of unequal
# lengths without truncation.
