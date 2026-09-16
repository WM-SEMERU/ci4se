def unknown(*args, **kwargs):
    name = kwargs.get('name', '')
    return '%s(%s)' % (name, ', '.join(str(a) for a in args))