def _load_point(tokens, string):
    if not next(tokens) == '(':
        raise ValueError(INVALID_WKT_FMT % string)
    coords = []
    try:
        for t in tokens:
            if t == ')':
                break
            else:
                coords.append(float(t))
    except tokenize.TokenError:
        raise ValueError(INVALID_WKT_FMT % string)
    return dict(type='Point', coordinates=coords)