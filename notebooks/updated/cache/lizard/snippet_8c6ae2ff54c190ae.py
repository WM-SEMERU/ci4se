def merge(cls, *args, **kwargs):
    newkeys = bool(kwargs.get('newkeys', False))
    ignore = kwargs.get('ignore', list())
    if len(args) < 1:
        raise ValueError('no ents given to Ent.merge()')
    elif not all(isinstance(s, Ent) for s in args):
        raise ValueError(
            'all positional arguments to Ent.merge() must be instances of Ent')
    ent = args[0]
    data = cls.load(ent)
    for ent in args[1:]:
        for key, value in ent.__dict__.items():
            if key in ignore:
                continue
            if key in data.__dict__:
                v1 = data.__dict__[key]
                if type(value) == type(v1):
                    if isinstance(v1, Ent):
                        data.__dict__[key] = cls.merge(v1, value, **kwargs)
                    else:
                        data.__dict__[key] = cls.load(value)
            elif newkeys:
                data.__dict__[key] = value
    return data