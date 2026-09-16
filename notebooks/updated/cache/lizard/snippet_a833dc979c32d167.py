def invalidate(*tables, **kwargs):
    backend = get_backend()
    db = kwargs.get('using', 'default')
    if backend._patched:
        for t in map(resolve_table, tables):
            backend.keyhandler.invalidate_table(t, db)