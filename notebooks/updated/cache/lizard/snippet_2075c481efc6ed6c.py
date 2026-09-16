def wrap_handler(self, api_types, methods, endpoints):

    def wrapper(fn):

        @wraps(fn)
        def wrapped(*args, **kwargs):
            return fn(*args, **kwargs)
        for api_type in api_types:
            for method in methods:
                for endpoint in endpoints:
                    key = api_type, method, endpoint
                    self._handler_chains.setdefault(key, [])
                    self._handler_chains[key].append(wrapped)
        return wrapped
    return wrapper