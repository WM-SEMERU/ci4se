def scramble_string(s, key):
    key = key_digits(key)
    for k in key:
        s = shift(s, key)
        s = s[k:] + s[:k]
        s = shuffle(s)
    return s