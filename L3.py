# Generators
# @ Michael


import memory_profiler as men_profile
import random
import time


# Compare methods with and without using generator


def square(nums):
    result = []
    for i in nums:
        result.append(i**2)
    return(result)


sq_nums = square([1, 2, 3, 4, 5])
print(sq_nums)


def sqr_gene(nums):
    for i in nums:
        yield i**2


sq_gen_nums = sqr_gene([1, 2, 3, 4])
print(sq_gen_nums)
print(next(sq_gen_nums))
print(next(sq_gen_nums))
# <generator object sqr_gene at 0x7fcbb0e5f5e8>
# 1
# 4


sq_gen_nums = sqr_gene([1, 2, 3, 4])
for num_it in sq_gen_nums:
    print(num_it)


# YIELD the result is the key!

# generator comprehension

my_num_ge = (x**2 for x in [1, 2, 3, 4, 5])
print(my_num_ge)
print(list(my_num_ge))

# Always trying to use generator
# Why ? Referece: https://www.youtube.com/watch?v=bD05uGo_sVI


names = ['John', 'Vishnu', 'Yulia', 'Emment', 'Kara']
majors = ['Math', 'Economics', 'Geology', 'Econometrics', 'Law']

print('Memory (before): {}Mb'.format(men_profile.memory_usage()))


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


# print(people_list(2))
# print(people_generator(2))

# t1 = time.process_time()
# people = people_list(1000000)
# t2 = time.process_time()

t1 = time.process_time()
people = people_generator(100000)
t2 = time.process_time()

print('Memory (after): {}Mb'.format(men_profile.memory_usage()))
print('Time Took {} Seconds'.format(t2-t1))

# List
# Memory (before): [88.41796875]Mb
# Memory (after): [324.89453125]Mb
# Time Took 3.5177499999999995 Seconds

# Generator
# Memory (before): [61.3515625]Mb
# Memory (after): [61.3515625]Mb
# Time Took 0.00013399999999919032 Seconds
