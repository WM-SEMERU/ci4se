def resource(self, uri, methods=frozenset({'GET'}), **kwargs):

    def decorator(f):
        if kwargs.get('stream'):
            f.is_stream = kwargs['stream']
        self.add_resource(f, uri=uri, methods=methods, **kwargs)
    return decorator