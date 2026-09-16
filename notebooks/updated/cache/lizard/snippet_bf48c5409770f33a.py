def build_insert(self, table, values, columns=None):
    if not columns:
        columns = table.columns
    if len(values) < len(columns):
        column_names = ','.join(columns[-len(values):])
    else:
        column_names = ','.join(columns)
    query = 'INSERT INTO %s (%s) VALUES (%s) ' % (table.name, column_names,
        ','.join(['?'] * len(values)))
    return query