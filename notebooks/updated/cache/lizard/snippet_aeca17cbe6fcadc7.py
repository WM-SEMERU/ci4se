def partition(list_, columns=2):
    iter_ = iter(list_)
    columns = int(columns)
    rows = []
    while True:
        row = []
        for column_number in range(1, columns + 1):
            try:
                value = six.next(iter_)
            except StopIteration:
                pass
            else:
                row.append(value)
        if not row:
            return rows
        rows.append(row)