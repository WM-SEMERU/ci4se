def many_init(cls, *args, **kwargs):
    allow_empty = kwargs.pop('allow_empty', None)
    child_serializer = cls(*args, **kwargs)
    list_kwargs = {'child': child_serializer}
    if allow_empty is not None:
        list_kwargs['allow_empty'] = allow_empty
    list_kwargs.update({key: value for key, value in kwargs.items() if key in
        LIST_SERIALIZER_KWARGS})
    meta = getattr(cls, 'Meta', None)
    list_serializer_class = getattr(meta, 'list_serializer_class',
        ListSerializer)
    return list_serializer_class(*args, **list_kwargs)