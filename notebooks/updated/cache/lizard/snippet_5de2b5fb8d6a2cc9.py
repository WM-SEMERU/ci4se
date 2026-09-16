def delete_table(cls):
    schema_editor = getattr(connection, 'schema_editor', None)
    if schema_editor:
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(cls)
    else:
        cursor = connection.cursor()
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings('ignore', 'unknown table')
                cursor.execute('DROP TABLE IF EXISTS {0}'.format(cls._meta.
                    db_table))
        finally:
            cursor.close()