def get_serialization_exclude(serializers, exclude, kwargs):
    exclude = list(exclude)
    options = [name.split('.')[0] for name in serializers]
    for key, value in kwargs.items():
        if key in ('vocab',) and value is False:
            deprecation_warning(Warnings.W015.format(arg=key))
            exclude.append(key)
        elif key.split('.')[0] in options:
            raise ValueError(Errors.E128.format(arg=key))
    return exclude