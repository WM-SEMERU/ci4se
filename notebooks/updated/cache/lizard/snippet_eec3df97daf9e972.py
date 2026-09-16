def encode(g, top=None, cls=PENMANCodec, **kwargs):
    codec = cls(**kwargs)
    return codec.encode(g, top=top)