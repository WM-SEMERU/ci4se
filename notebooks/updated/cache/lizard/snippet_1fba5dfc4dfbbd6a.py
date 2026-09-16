def __configure_annotations(mapper, cls):
    annotations = {}
    annotations_by_attr = {}
    processed = set()
    for base in cls.__mro__:
        for name, attr in base.__dict__.items():
            if name in processed or name.startswith('__'):
                continue
            if isinstance(attr, collections.Hashable) and attr in __cache__:
                data = __cache__[attr]
                del __cache__[attr]
            elif isinstance(attr, InstrumentedAttribute
                ) and attr.property in __cache__:
                data = __cache__[attr.property]
                del __cache__[attr.property]
            elif hasattr(attr, '_coaster_annotations'):
                data = attr._coaster_annotations
            else:
                data = None
            if data is not None:
                annotations_by_attr.setdefault(name, []).extend(data)
                for a in data:
                    annotations.setdefault(a, []).append(name)
                processed.add(name)
    if annotations:
        cls.__annotations__ = annotations
    if annotations_by_attr:
        cls.__annotations_by_attr__ = annotations_by_attr
    annotations_configured.send(cls)