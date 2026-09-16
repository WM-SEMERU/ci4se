def class_lookups(model_field):
    field_class = type(model_field)
    field_type = match_field(field_class)
    return get_field_lookups(field_type, model_field.null)