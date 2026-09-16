def wrap_session(func=None, *, storage=MemoryStorage):
    if func is None:
        return functools.partial(wrap_session, storage=storage)
    storage = storage()

    def wrapper(request, *args, **kwargs):
        session_key = storage.get_session_key(request)
        request.session = storage.retrieve(request, session_key)
        response = func(request, *args, **kwargs)
        storage.store(request, response, session_key, request.session)
        storage.persist_session_key(request, response, session_key)
        return response
    return wrapper