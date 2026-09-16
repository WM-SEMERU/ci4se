def append_md5_if_too_long(component, size):
    if len(component) > size:
        if size > 32:
            component_size = size - 32 - 1
            return '%s_%s' % (component[:component_size], hashlib.md5(
                component.encode('utf-8')).hexdigest())
        else:
            return hashlib.md5(component.encode('utf-8')).hexdigest()[:size]
    else:
        return component