my_dict = {'Egor': 2001, 'Eva': 1985, 'Sergey': 1997}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Eva'))
print('Not existing value:', my_dict.get('Masha'))
my_dict.update({'Sasha': 1995, 'Masha': 2003})
del my_dict['Egor']
print('Deleted value:', my_dict.get('Egor', 2001))
print('Modified dictionary:', my_dict)

my_set = {1, 2, 3, 4, 'ZZZ', True, 2, 3, 4, True}
my_set.add((7, 8, 9.89))
my_set.add(3.14)
my_set.remove('ZZZ')
print(my_set)
