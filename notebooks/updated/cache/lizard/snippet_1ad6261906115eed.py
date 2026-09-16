def __configure_roles(mapper, cls):
    if '__roles__' not in cls.__dict__:
        cls.__roles__ = deepcopy(cls.__roles__)
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
            elif hasattr(attr, '_coaster_roles'):
                data = attr._coaster_roles
            else:
                data = None
            if data is not None:
                for role in data.get('call', []):
                    cls.__roles__.setdefault(role, {}).setdefault('call', set()
                        ).add(name)
                for role in data.get('read', []):
                    cls.__roles__.setdefault(role, {}).setdefault('read', set()
                        ).add(name)
                for role in data.get('write', []):
                    cls.__roles__.setdefault(role, {}).setdefault('write',
                        set()).add(name)
                processed.add(name)