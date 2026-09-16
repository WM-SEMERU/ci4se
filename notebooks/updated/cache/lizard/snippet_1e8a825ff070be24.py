def to_foreign(self, obj, name, value):
    namespace = self.namespace
    try:
        explicit = self.explicit
    except AttributeError:
        explicit = not namespace
    if not isinstance(value, (str, unicode)):
        value = canon(value)
    if namespace and ':' in value:
        for point in iter_entry_points(namespace):
            qualname = point.module_name
            if point.attrs:
                qualname += ':' + '.'.join(point.attrs)
            if qualname == value:
                value = point.name
                break
    if ':' in value:
        if not explicit:
            raise ValueError('Explicit object references not allowed.')
        return value
    if namespace and value not in (i.name for i in iter_entry_points(namespace)
        ):
        raise ValueError('Unknown plugin "' + value + '" for namespace "' +
            namespace + '".')
    return value