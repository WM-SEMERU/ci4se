def create_engine(engine, options=None, defaults=None):
    if engine not in _ENGINE_MAP.keys():
        raise TTSError('Unknown engine %s' % engine)
    options = options or {}
    defaults = defaults or {}
    einst = _ENGINE_MAP[engine](**options)
    einst.configure_default(**defaults)
    return einst