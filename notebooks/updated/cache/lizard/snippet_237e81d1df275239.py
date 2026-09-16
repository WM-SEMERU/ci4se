def modify_fk_constraint(apps, schema_editor):
    model = apps.get_model('message_sender', 'OutboundSendFailure')
    table = model._meta.db_table
    with schema_editor.connection.cursor() as cursor:
        constraints = schema_editor.connection.introspection.get_constraints(
            cursor, table)
        [constraint] = filter(lambda c: c[1]['foreign_key'], constraints.
            items())
        [name, _] = constraint
    sql_delete_fk = (
        'SET CONSTRAINTS {name} IMMEDIATE; ALTER TABLE {table} DROP CONSTRAINT {name}'
        .format(table=schema_editor.quote_name(table), name=schema_editor.
        quote_name(name)))
    schema_editor.execute(sql_delete_fk)
    field = model.outbound.field
    to_table = field.remote_field.model._meta.db_table
    to_column = field.remote_field.model._meta.get_field(field.remote_field
        .field_name).column
    sql_create_fk = (
        'ALTER TABLE {table} ADD CONSTRAINT {name} FOREIGN KEY ({column}) REFERENCES {to_table} ({to_column}) ON DELETE CASCADE {deferrable};'
        .format(table=schema_editor.quote_name(table), name=schema_editor.
        quote_name(name), column=schema_editor.quote_name(field.column),
        to_table=schema_editor.quote_name(to_table), to_column=
        schema_editor.quote_name(to_column), deferrable=schema_editor.
        connection.ops.deferrable_sql()))
    schema_editor.execute(sql_create_fk)