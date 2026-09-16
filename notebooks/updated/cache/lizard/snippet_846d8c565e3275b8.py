def check_string(value, min_length=None, max_length=None, pattern=None):
    if type(value) not in [str, unicode]:
        return False
    if min_length and len(value) < min_length:
        return False
    if max_length and len(value) > max_length:
        return False
    if pattern and not re.match(pattern, value):
        return False
    return True