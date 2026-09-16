def action(cls, view):
    name = '%s:%s' % (cls.name, view.__name__)
    path = '%s/%s' % (cls.url, view.__name__)
    cls.actions.append((view.__doc__, path))
    return cls.register(path, name=name)(view)