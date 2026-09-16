def get_field(field):
    if isinstance(field, djmodels.fields.Field):
        return field
    elif isinstance(field, basestring):
        field = field.split('.')
        if len(field) == 3:
            model = get_model(app=field[0], model=field[1])
        elif len(field) == 2:
            model = get_model(app=DEFAULT_APP, model=field[0])
        else:
            return None
            raise NotImplementedError(
                "Unknown default model name. Don't know where to look for field %s"
                 % '.'.join(field))
        field = model._meta.get_field(field[-1])
    return field