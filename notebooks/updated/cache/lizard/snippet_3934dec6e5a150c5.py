def unpack(stream, **kwargs):
    msgpack_module = kwargs.pop('_msgpack_module', msgpack)
    return msgpack_module.unpack(stream, **kwargs)