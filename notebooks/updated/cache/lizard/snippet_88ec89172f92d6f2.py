def _LSAGuessPayloadClass(p, **kargs):
    cls = conf.raw_layer
    if len(p) >= 4:
        typ = p[3]
        clsname = _OSPF_LSclasses.get(typ, 'Raw')
        cls = globals()[clsname]
    return cls(p, **kargs)