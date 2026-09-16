def dispatch_hook(cls, _pkt=None, *args, **kargs):
    cls = conf.raw_layer
    if _pkt is not None:
        ptype = orb(_pkt[0])
        return globals().get(_param_set_cls.get(ptype), conf.raw_layer)
    return cls