def default_fields(cls, include_virtual=True, **kwargs):
    output = cls._staticfields.copy()
    if include_virtual:
        output.update({name: VIRTUALFIELD_DTYPE for name in cls._virtualfields}
            )
    return output