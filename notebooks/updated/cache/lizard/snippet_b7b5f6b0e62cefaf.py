def uni_to_beta(text):
    u = _UNICODE_MAP
    transform = []
    for ch in text:
        try:
            conv = u[ch]
        except KeyError:
            conv = ch
        transform.append(conv)
    converted = ''.join(transform)
    return converted