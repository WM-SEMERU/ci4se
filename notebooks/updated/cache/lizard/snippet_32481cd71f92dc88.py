def namedb_get_num_names_in_namespace(cur, namespace_id, current_block):
    unexpired_query, unexpired_args = namedb_select_where_unexpired_names(
        current_block)
    query = (
        'SELECT COUNT(name_records.name) FROM name_records JOIN namespaces ON name_records.namespace_id = namespaces.namespace_id WHERE name_records.namespace_id = ? AND '
         + unexpired_query + ' ORDER BY name;')
    args = (namespace_id,) + unexpired_args
    num_rows = namedb_select_count_rows(cur, query, args, count_column=
        'COUNT(name_records.name)')
    return num_rows