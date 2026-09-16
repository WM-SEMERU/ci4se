def dump(data, stream=None, Dumper=Dumper, **kwds):
    return dump_all([data], stream, Dumper=Dumper, **kwds)