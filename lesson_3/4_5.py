import random
import re


keys = list(map(str, [el for el in range(1, 11)]))
values = [el for el in range(1, 11)]


def write_file(filename, keys_list, values_list):
    for _ in range(len(keys)):
        if random.randint(0, 1) == 1:
            keys[_] = 'example' + keys[_]
    result_list = list(zip(keys_list, values_list))
    try:
        with open(filename, 'x') as f:
            for el in result_list:
                f.write(str(el) + '\n')
    except FileExistsError:
        print('File exists')
    read_file(filename)


def read_file(filename):
    with open(filename, 'r') as f:
        for el in f:
            el = el.strip()
            print(re.sub(r'example', r'number', el))


write_file('new', keys, values)
