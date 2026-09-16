def attribute(name, value, getter=None, setter=None, deleter=None, label=
    None, desc=None, meta=None):
    _annotate('attribute', name, value, getter=getter, setter=setter,
        deleter=deleter, label=label, desc=desc, meta=meta)