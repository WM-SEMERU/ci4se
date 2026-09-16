def serialize_query(func):

    @functools.wraps(func)
    def wrapper(self, query, *args, **kwargs):
        if hasattr(query, 'serialize'):
            query = query.serialize()
        assert isinstance(query, basestring), 'Expected query to be string'
        if self.debug:
            print('SQL:', query)
        return func(self, query, *args, **kwargs)
    return wrapper