immutable_var = 1, 'bbb', 4.35, True, [1, 2, 3]

# immutable_var[0] = 999
# кортеж относится к неизменяемым типам данных,
# изменять и редактировать его нельзя.

print('Immutable tuple: ', immutable_var)

mutable_list = [1, 'bbb', 4.35, True, [1, 2, 3]]
mutable_list[3] = ['modified', False, 3.14]
mutable_list[4][0] = 999
print('Mutable list: ', mutable_list)
