def create_engine(minsize=1, maxsize=10, loop=None, dialect=_dialect,
    pool_recycle=-1, compiled_cache=None, **kwargs):
    deprecated_cursor_classes = [DeserializationCursor, DictCursor,
        SSCursor, SSDictCursor]
    cursorclass = kwargs.get('cursorclass', Cursor)
    if not issubclass(cursorclass, Cursor) or any(issubclass(cursorclass,
        cursor_class) for cursor_class in deprecated_cursor_classes):
        raise ArgumentError(
            'SQLAlchemy engine does not support this cursor class')
    coro = _create_engine(minsize=minsize, maxsize=maxsize, loop=loop,
        dialect=dialect, pool_recycle=pool_recycle, compiled_cache=
        compiled_cache, **kwargs)
    return _EngineContextManager(coro)