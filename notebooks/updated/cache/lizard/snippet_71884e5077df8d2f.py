def _get_object_class(cls, class_name):
    class_name = class_name.lstrip(cls.__STRING_FORMAT_UNDERSCORE)
    if class_name in cls._override_field_map:
        class_name = cls._override_field_map[class_name]
    try:
        return getattr(endpoint, class_name)
    except AttributeError:
        pass
    try:
        return getattr(object_, class_name)
    except AttributeError:
        pass
    raise BunqException(cls._ERROR_MODEL_NOT_FOUND.format(class_name))