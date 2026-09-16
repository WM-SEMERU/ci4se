def to_commit(obj):
    if obj.type == 'tag':
        obj = deref_tag(obj)
    if obj.type != 'commit':
        raise ValueError('Cannot convert object %r to type commit' % obj)
    return obj