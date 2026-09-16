def _parse_boolean(value):
    value = value.lower()
    if value in _true_strings:
        return True
    elif value in _false_strings:
        return False
    else:
        return None