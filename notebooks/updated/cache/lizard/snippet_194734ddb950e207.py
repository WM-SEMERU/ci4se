def create_from_row(cls, table_row):
    kwargs = {}
    for key in table_row.colnames:
        kwargs[key] = table_row[key]
    try:
        return cls(**kwargs)
    except KeyError:
        print(kwargs)