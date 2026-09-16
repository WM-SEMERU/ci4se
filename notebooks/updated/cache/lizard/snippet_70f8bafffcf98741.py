def iter_extensions(prefix, event_id):
    extension = '{prefix}{event_id}'.format(prefix=prefix, event_id=event_id)
    yield extension
    suffix = 1
    while True:
        yield '{extension}{suffix}'.format(extension=extension, suffix=suffix)
        suffix += 1