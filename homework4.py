immutable_var = 1, 2, True, 'string'
print("immmutable_var: ", immutable_var)
# immutable_var[0] = 4 потомучто кортеж нужен когда нам надо сохранить исходные данные
mutable_list = [1, 2, True, 'string']
mutable_list[0] = 5
print('mutable_list: ', mutable_list)
