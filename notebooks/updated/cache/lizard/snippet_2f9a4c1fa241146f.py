def classify_class_attrs(cls):
    mro = getmro(cls)
    names = dir(cls)
    result = []
    for name in names:
        if name in cls.__dict__:
            obj = cls.__dict__[name]
        else:
            obj = getattr(cls, name)
        homecls = getattr(obj, '__objclass__', None)
        if homecls is None:
            for base in mro:
                if name in base.__dict__:
                    homecls = base
                    break
        if homecls is not None and name in homecls.__dict__:
            obj = homecls.__dict__[name]
        obj_via_getattr = getattr(cls, name)
        if isinstance(obj, staticmethod):
            kind = 'static method'
        elif isinstance(obj, classmethod):
            kind = 'class method'
        elif isinstance(obj, property):
            kind = 'property'
        elif ismethod(obj_via_getattr) or ismethoddescriptor(obj_via_getattr):
            kind = 'method'
        else:
            kind = 'data'
        result.append((name, kind, homecls, obj))
    return result