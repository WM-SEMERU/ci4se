def mapping_of(cls):

    def mapper(data):
        if not isinstance(data, Mapping):
            raise TypeError('data must be a mapping, not %s' % type(data).
                __name__)
        return {key: cls(value) for key, value in data.items()}
    return mapper