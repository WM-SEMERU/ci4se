def create_table(cls):
    schema_editor = getattr(connection, 'schema_editor', None)
    if schema_editor:
        with schema_editor() as schema_editor:
            schema_editor.create_model(cls)
    else:
        raw_sql, _ = connection.creation.sql_create_model(cls, no_style(), [])
        cls.delete_table()
        cursor = connection.cursor()
        try:
            cursor.execute(*raw_sql)
        finally:
            cursor.close()