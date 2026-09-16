def format_value(column_dict, value, key=None):
    formatter = column_dict.get('formatter')
    prop = column_dict['__col__']
    res = value
    if value in ('', None):
        res = ''
    elif formatter is not None:
        res = formatter(value)
    elif hasattr(prop, 'columns'):
        sqla_column = prop.columns[0]
        column_type = getattr(sqla_column.type, 'impl', sqla_column.type)
        formatter = FORMATTERS_REGISTRY.get_formatter(column_type, key)
        if formatter is not None:
            res = formatter(value)
    return res