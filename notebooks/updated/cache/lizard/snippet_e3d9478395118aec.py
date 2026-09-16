def PointCollection(mode='raw', *args, **kwargs):
    if mode == 'raw':
        return RawPointCollection(*args, **kwargs)
    return AggPointCollection(*args, **kwargs)