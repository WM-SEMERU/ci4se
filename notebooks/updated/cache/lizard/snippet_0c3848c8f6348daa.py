def encrypt_password(**kwargs):
    new_value = kwargs['new_value']
    field = kwargs['field']
    min_length = field.params['min_length']
    if len(new_value) < min_length:
        raise ValueError('`{}`: Value length must be more than {}'.format(
            field.name, field.params['min_length']))
    if new_value and not crypt.match(new_value):
        new_value = str(crypt.encode(new_value))
    return new_value