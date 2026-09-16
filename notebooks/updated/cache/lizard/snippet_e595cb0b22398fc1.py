def String(length=None, **kwargs):
    return Property(length=length, types=stringy_types, convert=to_string,
        **kwargs)