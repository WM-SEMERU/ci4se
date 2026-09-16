def chunk_cache(method):

    @functools.wraps(method)
    def wrapper(self, context):
        if not self._is_cached:
            return method(self, context)
        name = context.name
        idx = context.array_extents(name)
        key = tuple(i for t in idx for i in t)
        array_cache = self._chunk_cache[name]
        if key not in array_cache:
            array_cache[key] = method(self, context)
        return array_cache[key]
    f = wrapper
    f.__decorator__ = chunk_cache.__name__
    return f