def get_all(self, fields=list(), limit=None, order_by=list(), offset=None):
    warnings.warn('get_all() is deprecated, please use get_multiple() instead',
        DeprecationWarning)
    return self.get_multiple(fields, limit, order_by, offset)