def loads(data, cls=PVLDecoder, strict=True, **kwargs):
    decoder = __create_decoder(cls, strict, **kwargs)
    if not isinstance(data, bytes):
        data = data.encode('utf-8')
    return decoder.decode(data)