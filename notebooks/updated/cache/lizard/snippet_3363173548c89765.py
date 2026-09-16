def copy_from_csv_sql(qualified_name: str, delimiter=',', encoding='utf8',
    null_str='', header=True, escape_str='\\', quote_char='"',
    force_not_null=None, force_null=None):
    options = []
    options.append("DELIMITER '%s'" % delimiter)
    options.append("NULL '%s'" % null_str)
    if header:
        options.append('HEADER')
    options.append("QUOTE '%s'" % quote_char)
    options.append("ESCAPE '%s'" % escape_str)
    if force_not_null:
        options.append(_format_force_not_null(column_names=force_not_null))
    if force_null:
        options.append(_format_force_null(column_names=force_null))
    postgres_encoding = get_postgres_encoding(encoding)
    options.append("ENCODING '%s'" % postgres_encoding)
    copy_sql = _format_copy_csv_sql(qualified_name, copy_options=options)
    return copy_sql