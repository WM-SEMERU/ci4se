def RegexField(regex, default=NOTHING, required=True, repr=True, cmp=True,
    key=None):
    default = _init_fields.init_default(required, default, None)
    validator = _init_fields.init_validator(required, string_types,
        validators.regex(regex))
    return attrib(default=default, converter=converters.str_if_not_none,
        validator=validator, repr=repr, cmp=cmp, metadata=dict(key=key))