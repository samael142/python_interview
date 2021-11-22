num = input('Input number: ')
if '.' in num:
    print('Дробное')
    num_list = list(map(int, num.split('.')))
    if num_list[0] == num_list[1]:
        print(True)
    else:
        print(False)
else:
    print('Целое')
