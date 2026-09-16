def handle_fobj(backend, f, **kwargs):
    if not is_binary(f):
        raise AssertionError('File must be opened in binary mode.')
    if callable(getattr(backend, 'handle_fobj', None)):
        LOGGER.debug('using handle_fobj')
        return backend.handle_fobj(f)
    elif callable(getattr(backend, 'handle_path', None)):
        LOGGER.debug('using handle_path')
        LOGGER.warning(
            'Using disk, %r backend does not provide `handle_fobj()`', backend)
        ext = ''
        if 'ext' in kwargs:
            ext = '.' + kwargs['ext']
        with fobj_to_tempfile(f, suffix=ext) as fname:
            return backend.handle_path(fname, **kwargs)
    else:
        raise AssertionError('Backend %s has no _get functions' % backend.
            __name__)