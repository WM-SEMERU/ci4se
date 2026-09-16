def get_name(component):
    if six.callable(component):
        name = getattr(component, '__qualname__', component.__name__)
        return '.'.join([component.__module__, name])
    return str(component)