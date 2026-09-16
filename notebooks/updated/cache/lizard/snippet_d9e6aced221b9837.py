def wrap_arguments(args=None):
    if args is None:
        args = []
    tags = []
    for name, value in args:
        tag = '<{name}>{value}</{name}>'.format(name=name, value=escape(
            '%s' % value, {'"': '&quot;'}))
        tags.append(tag)
    xml = ''.join(tags)
    return xml