def print_params(a=1, b='free', c=True):
    print(a, b, c)


print_params()
print_params(1, 2,)
print_params(b = 25)
print_params(c = [1, 2, 3])

def print_params(a, b, c):
    print(a, b, c)


values_list_2 = ['str', True]
values_list = [1, 2]
values_dict = {'c': 3}
print_params(*values_list, **values_dict)
print_params(*values_list_2, 42)
