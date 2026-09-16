def cache_key(self, method_name):
    key = ''
    method = getattr(self, 'cache_key_{}'.format(method_name), None)
    if method:
        key = method()
    return key