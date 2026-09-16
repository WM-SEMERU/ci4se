def convert_numeric_id_to_id36(numeric_id):
    if not isinstance(numeric_id, six.integer_types) or numeric_id < 0:
        raise ValueError('must supply a positive int/long')
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    alphabet_len = len(alphabet)
    current_number = numeric_id
    base36 = []
    if 0 <= current_number < alphabet_len:
        return alphabet[current_number]
    while current_number != 0:
        current_number, rem = divmod(current_number, alphabet_len)
        base36.append(alphabet[rem])
    return ''.join(reversed(base36))