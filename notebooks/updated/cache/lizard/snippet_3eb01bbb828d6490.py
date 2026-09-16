def set_char(key, value):
    global _chars
    category = _get_char_category(key)
    if not category:
        raise KeyError
    _chars[category][key] = value