def best_match(requested, allowed):
    requested = [parse_ctype(ctype) for ctype in quoted_split(requested, ',')]
    best_q = -1
    best_ctype = ''
    best_params = {}
    best_match = '*/*'
    for ctype in allowed:
        for ctype_mask, params in requested:
            try:
                q = float(params.get('q', 1.0))
            except ValueError:
                continue
            if q < best_q:
                continue
            elif best_q == q:
                if best_match.count('*') <= ctype_mask.count('*'):
                    continue
            if _match_mask(ctype_mask, ctype):
                best_q = q
                best_ctype = ctype
                best_params = params
                best_match = ctype_mask
    return best_ctype, best_params