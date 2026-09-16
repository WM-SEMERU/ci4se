def normalize_input_value(value):
    if value in ('blank', 'ignore', 'inherit'):
        return value
    tokens = value.split(':')
    if len(tokens) < 2 or tokens[0] not in ('text', 'env', 'cred', 'key',
        'array'):
        return 'text:%s' % value
    return value