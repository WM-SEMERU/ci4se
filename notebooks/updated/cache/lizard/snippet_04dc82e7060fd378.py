def validate_value_type(value, spec):
    if 'maxlen' in spec:
        return len(value) <= int(spec['maxlen'])
    if spec['base'] == 'string':
        if 'enumeration' in spec:
            if value not in spec['enumeration']:
                raise NotValid('value not in enumeration')
        else:
            return valid_string(value)
    elif spec['base'] == 'list':
        for val in [v.strip() for v in value.split(',')]:
            valid(spec['member'], val)
    else:
        return valid(spec['base'], value)
    return True