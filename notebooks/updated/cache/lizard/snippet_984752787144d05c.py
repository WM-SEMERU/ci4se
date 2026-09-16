def validate(data, schema, defined_keys=False):
    if isinstance(data, dict):
        validator = Validator(data, schema, defined_keys=defined_keys)
        validator.validate()
    else:
        raise TypeError('expected data to be of type dict, but got: %s' %
            type(data))