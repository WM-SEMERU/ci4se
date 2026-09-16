def multiply(self, a, b):
    if a is None or b is None:
        return None
    m, n = len(a), len(b[0])
    if len(b) != n:
        raise Exception("A's column number must be equal to B's row number.")
    l = len(b[0])
    table_a, table_b = {}, {}
    for i, row in enumerate(a):
        for j, ele in enumerate(row):
            if ele:
                if i not in table_a:
                    table_a[i] = {}
                table_a[i][j] = ele
    for i, row in enumerate(b):
        for j, ele in enumerate(row):
            if ele:
                if i not in table_b:
                    table_b[i] = {}
                table_b[i][j] = ele
    c = [[(0) for j in range(l)] for i in range(m)]
    for i in table_a:
        for k in table_a[i]:
            if k not in table_b:
                continue
            for j in table_b[k]:
                c[i][j] += table_a[i][k] * table_b[k][j]
    return c