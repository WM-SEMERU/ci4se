def convert_boolean(string_value):
    lean_string_value = string_value.strip().lower()
    if lean_string_value in ['yes', 'true', 'on', '1']:
        return True
    elif lean_string_value in ['no', 'false', 'off', '0']:
        return False
    raise ValueError('Unrecognised boolean ({})'.format(lean_string_value))