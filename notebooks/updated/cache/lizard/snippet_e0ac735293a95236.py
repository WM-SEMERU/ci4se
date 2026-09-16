def table_to_intermediary(table):
    return Table(name=table.fullname, columns=[column_to_intermediary(col) for
        col in table.c._data.values()])