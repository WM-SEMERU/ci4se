def cname(cls, map_name, container, instance=None):
    if instance:
        return '{0}.{1}.{2}'.format(map_name, container, instance)
    return '{0}.{1}'.format(map_name, container)