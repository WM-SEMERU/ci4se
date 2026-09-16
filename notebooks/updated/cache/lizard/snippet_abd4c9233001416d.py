def split_number_and_unit(s):
    if not s:
        raise ValueError('empty value')
    s = s.strip()
    pos = len(s)
    while pos and not s[pos - 1].isdigit():
        pos -= 1
    number = int(s[:pos])
    unit = s[pos:].strip()
    return number, unit