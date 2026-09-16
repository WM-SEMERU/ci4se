def _IsMap(message, field):
    value = message.get_assigned_value(field.name)
    if not isinstance(value, messages.Message):
        return False
    try:
        additional_properties = value.field_by_name('additionalProperties')
    except KeyError:
        return False
    else:
        return additional_properties.repeated