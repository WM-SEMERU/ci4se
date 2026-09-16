def build_insert(table_name, attributes):
    sql = 'INSERT INTO %s' % table_name
    column_str = ''
    value_str = ''
    for index, (key, value) in enumerate(attributes.items()):
        if index > 0:
            column_str += ','
            value_str += ','
        column_str += key
        value_str += value_to_sql_str(value)
    sql = sql + '(%s) VALUES(%s)' % (column_str, value_str)
    return sql