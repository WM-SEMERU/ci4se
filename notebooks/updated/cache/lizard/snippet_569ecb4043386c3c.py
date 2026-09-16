def from_string(value):
    if value == None or len(value) == 0:
        return None
    tokens = value.split(',')
    if len(tokens) == 1:
        return TypeDescriptor(tokens[0].strip(), None)
    elif len(tokens) == 2:
        return TypeDescriptor(tokens[0].strip(), tokens[1].strip())
    else:
        raise ConfigException(None, 'BAD_DESCRIPTOR', 'Type descriptor ' +
            value + ' is in wrong format').with_details('descriptor', value)