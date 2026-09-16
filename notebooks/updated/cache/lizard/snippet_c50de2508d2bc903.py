def build_method_map(self, prototype, prefix=''):
    if not isinstance(prototype, dict):
        prototype = dict((method, getattr(prototype, method)) for method in
            dir(prototype) if not method.startswith('_'))
    for attr, method in prototype.items():
        if callable(method):
            self[prefix + attr] = method