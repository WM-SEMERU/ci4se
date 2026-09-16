def build_schema_info(connection_alias):
    connection = get_valid_connection(connection_alias)
    ret = []
    with connection.cursor() as cursor:
        tables_to_introspect = connection.introspection.table_names(cursor,
            include_views=_include_views())
        for table_name in tables_to_introspect:
            if not _include_table(table_name):
                continue
            td = []
            table_description = connection.introspection.get_table_description(
                cursor, table_name)
            for row in table_description:
                column_name = row[0]
                try:
                    field_type = connection.introspection.get_field_type(row
                        [1], row)
                except KeyError as e:
                    field_type = 'Unknown'
                td.append((column_name, field_type))
            ret.append((table_name, td))
    return ret