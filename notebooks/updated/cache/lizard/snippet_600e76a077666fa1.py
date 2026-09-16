def process_base_field(cls, field, key):
    if not field.name:
        field.name = key
    elif key != field.name:
        if not isinstance(field.alias, list):
            field.alias = [key]
        else:
            field.alias.insert(0, key)
        setattr(cls, field.name, field)
    cls.prepare_field(field)
    if field.alias:
        for alias_name in field.alias:
            if key is not alias_name:
                setattr(cls, alias_name, field)