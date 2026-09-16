def split_string_at_suffix(s, numbers_into_suffix=False):
    if not s:
        return s, ''
    pos = len(s)
    while pos and numbers_into_suffix == s[pos - 1].isdigit():
        pos -= 1
    return s[:pos], s[pos:]