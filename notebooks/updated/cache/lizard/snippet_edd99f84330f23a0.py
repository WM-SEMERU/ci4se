def _dispatch(self, method, params):
    func = None
    try:
        func = self.funcs[method]
    except KeyError:
        if self.instance is not None:
            if hasattr(self.instance, '_dispatch'):
                return self.instance._dispatch(method, params)
            else:
                try:
                    func = resolve_dotted_attribute(self.instance, method,
                        self.allow_dotted_names)
                except AttributeError:
                    pass
    if func is not None:
        return func(*params)
    else:
        raise Exception('method "%s" is not supported' % method)