def StringIO(*args, **kwargs):
    raw = sync_io.StringIO(*args, **kwargs)
    return AsyncStringIOWrapper(raw)