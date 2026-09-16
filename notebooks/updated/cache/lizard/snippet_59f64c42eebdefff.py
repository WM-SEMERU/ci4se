def validate_complex(prop, value, xpath_map=None):
    if value is not None:
        validate_type(prop, value, dict)
        if prop in _complex_definitions:
            complex_keys = _complex_definitions[prop]
        else:
            complex_keys = {} if xpath_map is None else xpath_map
        for complex_prop, complex_val in iteritems(value):
            complex_key = '.'.join((prop, complex_prop))
            if complex_prop not in complex_keys:
                _validation_error(prop, None, value, 'keys: {0}'.format(','
                    .join(complex_keys)))
            validate_type(complex_key, complex_val, (string_types, list))