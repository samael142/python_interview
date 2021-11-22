import os


def get_file_name(file_name):
    return os.path.basename(file_name).split('.')[0]


print(get_file_name("//share/file.txt"))
