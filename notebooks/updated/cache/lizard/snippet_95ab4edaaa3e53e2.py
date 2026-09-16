def get_unique_fields(cls):
    unique_fields = []
    for fname, field in cls.__dict__.items():
        if isinstance(field, models.fields.Field):
            if getattr(field, 'unique', False):
                try:
                    field.unique = False
                except AttributeError:
                    field._unique = False
                unique_fields.append(fname)
    return unique_fields