def object(self, object):
    if object is None:
        raise ValueError('Invalid value for `object`, must not be `None`')
    allowed_values = ['service-package-quota-history']
    if object not in allowed_values:
        raise ValueError('Invalid value for `object` ({0}), must be one of {1}'
            .format(object, allowed_values))
    self._object = object