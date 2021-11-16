def multiplication_table(a, b):
    for el_a in range(1, a + 1):
        row = []
        for el_b in range(1, b + 1):
            row.append(f"{el_a} * {el_b} = {el_a * el_b}")
        print(f(row))


f = lambda f: '    '.join(f)

multiplication_table(10, 10)
