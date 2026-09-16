def path(value, allow_empty=False, **kwargs):
    if not value and not allow_empty:
        raise errors.EmptyValueError('value (%s) was empty' % value)
    elif not value:
        return None
    if hasattr(os, 'PathLike'):
        if not isinstance(value, (str, bytes, int, os.PathLike)):
            raise errors.NotPathlikeError('value (%s) is path-like' % value)
    elif not isinstance(value, int):
        try:
            os.path.exists(value)
        except TypeError:
            raise errors.NotPathlikeError('value (%s) is not path-like' % value
                )
    return value