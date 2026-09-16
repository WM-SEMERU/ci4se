def comment_thread(cls, backend, *args, **kwargs):
    ct_cls = cls._known_backends.get(backend)
    if not ct_cls:
        return None
    return ct_cls(*args, **kwargs)