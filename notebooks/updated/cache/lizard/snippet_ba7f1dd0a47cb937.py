def pertotal(table, option):
    if option == 'table':
        total = sum([i for line in table for i in line])
    t = []
    for row in table:
        t_row = []
        if option != 'table':
            total = sum(row)
        for i in row:
            if total == 0:
                t_row.append(0)
            else:
                t_row.append(i / total * 100)
        t.append(t_row)
    return t