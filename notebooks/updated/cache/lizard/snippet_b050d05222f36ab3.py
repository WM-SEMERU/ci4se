def change_column_name(conn, table, old_column_name, new_column_name,
    schema=None):
    activity_table = get_activity_table(schema=schema)
    query = activity_table.update().values(old_data=jsonb_change_key_name(
        activity_table.c.old_data, old_column_name, new_column_name),
        changed_data=jsonb_change_key_name(activity_table.c.changed_data,
        old_column_name, new_column_name)).where(activity_table.c.
        table_name == table)
    return conn.execute(query)