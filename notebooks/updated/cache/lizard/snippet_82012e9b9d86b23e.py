def is_none(string_, default='raise'):
    none = ['none', 'undefined', 'unknown', 'null', '']
    if string_.lower() in none:
        return True
    elif not default:
        return False
    else:
        raise ValueError("The value '{}' cannot be mapped to none.".format(
            string_))