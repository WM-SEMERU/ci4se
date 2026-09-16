def handle_new(path, **kwargs):
    log.info('new: %s %s' % (path, kwargs))
    repo = Local.new(path=path, **kwargs)
    return repo.serialize()