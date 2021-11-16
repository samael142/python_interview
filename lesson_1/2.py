import os


def print_directory_contents(path):
    for el in os.listdir(path):
        print(f'{path}/{el}')
    for el in os.listdir(path):
        if os.path.isdir(os.path.join(path, el)):
            print_directory_contents(os.path.join(path, el))


print(print_directory_contents('/Users/sergey_filippenkov/test'))
