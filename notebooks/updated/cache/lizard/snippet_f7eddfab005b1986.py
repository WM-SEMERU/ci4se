def update_from_object(self, obj, criterion=lambda key: key.isupper()):
    log.debug('Loading config from {0}'.format(obj))
    if isinstance(obj, basestring):
        if '.' in obj:
            path, name = obj.rsplit('.', 1)
            mod = __import__(path, globals(), locals(), [name], 0)
            obj = getattr(mod, name)
        else:
            obj = __import__(obj, globals(), locals(), [], 0)
    self.update((key, getattr(obj, key)) for key in filter(criterion, dir(obj))
        )