def clear(**kwargs):
    database = kwargs.pop('database', False)
    expression = lambda target, table: table.drop(target)
    test = lambda x, tab: not database_exists(x.url) or not tab.exists(x)
    if database and database_exists(engine['default'].url):
        drop_database(engine['default'].url)
        clear_cache()
    op(expression, reversed(metadata.sorted_tables), test=test, primary=
        'clear', secondary='drop', **kwargs)