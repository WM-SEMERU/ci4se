def set_query(self, value):
    if isinstance(value, basestring) or value is None:
        self._content['query'] = value
    elif hasattr(value, 'keys'):
        self._content['query'] = query.terms_from_dict(value)
    else:
        raise TypeError('Query must be a string or dict. Got: ' + type(
            value) + ' insted!')