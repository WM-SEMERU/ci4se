def parse_literal(x):
    if isinstance(x, list):
        return [parse_literal(y) for y in x]
    elif isinstance(x, (bytes, str)):
        try:
            return int(x)
        except ValueError:
            try:
                return float(x)
            except ValueError:
                return x
    else:
        raise TypeError('input must be a string or a list of strings')