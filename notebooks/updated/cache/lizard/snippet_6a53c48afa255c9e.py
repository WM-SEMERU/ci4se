def rate_limited(self, key_function=None):
    if key_function is None:

        def key_function(*args, **kwargs):
            data = pickle.dumps((args, sorted(kwargs.items())))
            return hashlib.md5(data).hexdigest()

    def decorator(fn):

        @wraps(fn)
        def inner(*args, **kwargs):
            key = key_function(*args, **kwargs)
            if self.limit(key):
                raise RateLimitException(
                    'Call to %s exceeded %s events in %s seconds.' % (fn.
                    __name__, self._limit, self._per))
            return fn(*args, **kwargs)
        return inner
    return decorator