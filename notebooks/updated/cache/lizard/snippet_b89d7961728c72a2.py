def query(self, query):
    if query is None:
        raise ValueError('Invalid value for `query`, must not be `None`')
    if query is not None and len(query) > 1000:
        raise ValueError(
            'Invalid value for `query`, length must be less than or equal to `1000`'
            )
    self._query = query