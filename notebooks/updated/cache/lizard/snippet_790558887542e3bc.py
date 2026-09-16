def tag(*tags):

    def dfn(fn):
        _tags = getattr(fn, 'tags', set())
        _tags.update(tags)
        fn.tags = _tags
        return fn
    return dfn