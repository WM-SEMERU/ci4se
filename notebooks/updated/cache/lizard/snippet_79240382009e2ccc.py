def _parse_vars(self, tokens):
    key_values = {}
    for token in tokens:
        if token.startswith('#'):
            break
        else:
            k, v = token.split('=', 1)
            key = k.strip()
            key_values[key] = v.strip()
    return key_values