def snake_to_camel(s, upper=True):
    s = _re_snake_to_camel.sub(lambda m: m.group(2).upper(), s)
    if upper:
        s = s[:1].upper() + s[1:]
    return s