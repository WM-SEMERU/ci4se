def get_column_names(context, query):
    table_info = context.sql_client.send(query)
    if 'fields' in table_info:
        return table_info['fields']
    return None