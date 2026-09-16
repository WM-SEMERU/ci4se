def get_bind_processor(column_type, dialect):
    if column_type.compile(dialect) not in {'JSON', 'JSONB'}:
        return column_type.bind_processor(dialect)
    if type(column_type) in {JSON, JSONB}:
        return None
    elif isinstance(column_type, TypeDecorator
        ) and column_type._has_bind_processor:
        return partial(column_type.process_bind_param, dialect=dialect)
    else:

        def wrapped_bind_processor(value):
            json_deserializer = dialect._json_deserializer or json.loads
            return json_deserializer(column_type.bind_processor(dialect)(value)
                )
        return wrapped_bind_processor