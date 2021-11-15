"""Не понял задание"""

import time


def random_number(start_num, end_num):
    number = start_num + time.time_ns() % (end_num - start_num)
    return number


print(random_number(1, 100))
