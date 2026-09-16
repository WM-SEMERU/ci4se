def _check_unique_together(cls):
    if cls._meta.unique_together is None:
        return
    if not isinstance(cls._meta.unique_together, (tuple, list)):
        raise ConfigurationError(
            "'{}.unique_together' must be a list or tuple.".format(cls.
            __name__))
    elif any(not isinstance(unique_fields, (tuple, list)) for unique_fields in
        cls._meta.unique_together):
        raise ConfigurationError(
            "All '{}.unique_together' elements must be lists or tuples.".
            format(cls.__name__))
    else:
        for fields_tuple in cls._meta.unique_together:
            for field_name in fields_tuple:
                field = cls._meta.fields_map.get(field_name)
                if not field:
                    raise ConfigurationError(
                        "'{}.unique_together' has no '{}' field.".format(
                        cls.__name__, field_name))
                if isinstance(field, ManyToManyField):
                    raise ConfigurationError(
                        "'{}.unique_together' '{}' field refers to ManyToMany field."
                        .format(cls.__name__, field_name))