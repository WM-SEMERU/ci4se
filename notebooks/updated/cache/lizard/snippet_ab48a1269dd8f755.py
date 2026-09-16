def handle_path(backend_inst, path, **kwargs):
    if callable(getattr(backend_inst, 'handle_path', None)):
        LOGGER.debug('using handle_path')
        return backend_inst.handle_path(path)
    elif callable(getattr(backend_inst, 'handle_fobj', None)):
        LOGGER.debug('using handle_fobj')
        with open(path, 'rb') as f:
            return backend_inst.handle_fobj(f)
    else:
        raise AssertionError('Backend %s has no _get functions' %
            backend_inst.__name__)