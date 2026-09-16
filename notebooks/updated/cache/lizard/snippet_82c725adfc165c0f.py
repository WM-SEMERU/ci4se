def subclass(cls, vt_code, vt_args):
    from geoid import get_class
    import geoid.census
    parser = get_class(geoid.census, vt_args.strip('/')).parse
    cls = type(vt_code.replace('/', '_'), (cls,), {'vt_code': vt_code,
        'parser': parser})
    globals()[cls.__name__] = cls
    assert cls.parser
    return cls