def encode(*args, **kwargs):
    encoding = kwargs.pop('encoding', DEFAULT_ENCODING)
    encoder = get_encoder(encoding, **kwargs)
    [encoder.writeElement(el) for el in args]
    stream = encoder.stream
    stream.seek(0)
    return stream