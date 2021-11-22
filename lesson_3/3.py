keys_list_1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eighth']
values_list_1 = [1, 2, 3, 4, 5, 6]
keys_list_2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eighth']
values_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_dict_from_lists(keys, values):
    result_dict = {}
    for key in range(len(keys)):
        try:
            result_dict[keys[key]] = values[key]
        except IndexError:
            result_dict[keys[key]] = None
    return result_dict


print(get_dict_from_lists(keys_list_1, values_list_1))
print(get_dict_from_lists(keys_list_2, values_list_2))
