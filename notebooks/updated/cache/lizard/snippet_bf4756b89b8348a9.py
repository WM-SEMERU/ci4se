def DateField(formatter=types.DEFAULT_DATE_FORMAT, default=NOTHING,
    required=True, repr=True, cmp=True, key=None):
    default = _init_fields.init_default(required, default, None)
    validator = _init_fields.init_validator(required, date)
    converter = converters.to_date_field(formatter)
    return attrib(default=default, converter=converter, validator=validator,
        repr=repr, cmp=cmp, metadata=dict(formatter=formatter, key=key))