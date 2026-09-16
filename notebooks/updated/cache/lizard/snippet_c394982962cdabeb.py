def dump(module, stream, cls=PVLEncoder, **kwargs):
    if isinstance(stream, six.string_types):
        with open(stream, 'wb') as fp:
            return cls(**kwargs).encode(module, fp)
    cls(**kwargs).encode(module, stream)