def connect(url=None, schema=None, reflect_metadata=True, engine_kwargs=
    None, reflect_views=True, ensure_schema=True, row_type=row_type):
    if url is None:
        url = os.environ.get('DATABASE_URL', 'sqlite://')
    return Database(url, schema=schema, reflect_metadata=reflect_metadata,
        engine_kwargs=engine_kwargs, reflect_views=reflect_views,
        ensure_schema=ensure_schema, row_type=row_type)