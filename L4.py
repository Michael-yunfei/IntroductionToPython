# List Comprehension
# @ Michael
# Reference: https://www.youtube.com/watch?v=3dt4OGnU5sM

sequence = [1, 2, 3, 4, 5, 6, 7, 8]

my_lst = [n*2 for n in sequence]
print(my_lst)

my_lst2 = [n for n in sequence if n % 2 == 0]  # you can add if condition
print(my_lst2)

# You can even do pairs with list comprehension

my_lst3 = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_lst3)
# [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2),
# ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('d', 0), ('d', 1),
# ('d', 2), ('d', 3)]

Names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade', 'Yulia']
Heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool', 'Beauty']
print(zip(Names, Heros))

my_dict = {}
for name, hero in zip(Names, Heros):
    my_dict[name] = hero
print(my_dict)

my_dict = {name: hero for name, hero in zip(Names, Heros)}
print(my_dict)

my_dict2 = {name: hero for name, hero in zip(Names, Heros) if name != 'Peter'}
print(my_dict2)
