my_list = [23, None, -77, 'True', True, 59.7]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)