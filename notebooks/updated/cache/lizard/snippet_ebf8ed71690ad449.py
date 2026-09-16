def _get_tokens_and_tags(parse_str):
    tokens = []
    parse_split = parse_str.split(' ')
    for p in parse_split:
        assert p.startswith('(') or p.endswith(')')
        if p.endswith(')'):
            token = p.replace(')', '')
            tokens.append(token)
    return tokens