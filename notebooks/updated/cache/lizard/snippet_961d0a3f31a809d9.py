def make_routing_table(obj, keys, prefix='on_'):

    def maptuple(k):
        if isinstance(k, tuple):
            if len(k) == 2:
                return k
            elif len(k) == 1:
                return k[0], lambda *aa, **kw: getattr(obj, prefix + k[0])(*
                    aa, **kw)
            else:
                raise ValueError()
        else:
            return k, lambda *aa, **kw: getattr(obj, prefix + k)(*aa, **kw)
    return dict([maptuple(k) for k in keys])