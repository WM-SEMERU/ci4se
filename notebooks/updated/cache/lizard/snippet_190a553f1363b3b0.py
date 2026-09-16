def match(self, methods, request_method):
    if isinstance(methods, basestring):
        return {} if request_method == methods else None
    return {} if request_method in methods else None