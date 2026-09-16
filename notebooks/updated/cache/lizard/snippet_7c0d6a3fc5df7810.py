def string_to_boolean(value, strict=False, default_value=False):
    if is_undefined(value) and default_value:
        return default_value
    if isinstance(value, bool):
        return value
    if isinstance(value, basestring) and value is not None:
        value = value.lower()
    is_true = value in ('yes', 'true', 't', '1')
    if not is_true and strict == True and value not in ('no', 'false', 'f', '0'
        ):
        raise ValueError(
            "The specified string doesn't represent a boolean value")
    return is_true