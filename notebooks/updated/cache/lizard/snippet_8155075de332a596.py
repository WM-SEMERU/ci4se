def is_valid_int(value):
    if 0 <= value <= Parameter.MAX:
        return True
    if value == Parameter.UNKNOWN_VALUE:
        return True
    if value == Parameter.CURRENT_POSITION:
        return True
    return False