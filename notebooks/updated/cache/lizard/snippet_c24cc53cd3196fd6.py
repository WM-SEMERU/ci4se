def column_describe(table_name, col_name):
    col_desc = orca.get_table(table_name).get_column(col_name).describe()
    return col_desc.to_json(orient='split'), 200, {'Content-Type':
        'application/json'}