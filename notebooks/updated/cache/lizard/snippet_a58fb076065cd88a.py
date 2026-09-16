def construct_field(model_name, field_name, field_type, all_models, **kwargs):
    field_type_parts = field_type.split('->')
    _field_type = field_type_parts[0].strip().split('[]')[0].strip()
    back_populates = field_type_parts[1].strip() if len(field_type_parts
        ) > 1 else None
    error_context = kwargs.pop('error_context', StatikErrorContext())
    _kwargs = copy(kwargs)
    _kwargs['back_populates'] = back_populates
    if _field_type not in FIELD_TYPES and _field_type not in all_models:
        raise InvalidFieldTypeError(model_name, field_name, context=
            error_context)
    if _field_type in FIELD_TYPES:
        return FIELD_TYPES[_field_type](field_name, **_kwargs)
    if field_type_parts[0].strip().endswith('[]'):
        return StatikManyToManyField(field_name, _field_type, **_kwargs)
    return StatikForeignKeyField(field_name, _field_type, **_kwargs)