def parse_personalities(personalities_line):
    tokens = personalities_line.split()
    assert tokens.pop(0) == 'Personalities'
    assert tokens.pop(0) == ':'
    personalities = []
    for token in tokens:
        assert token.startswith('[') and token.endswith(']')
        personalities.append(token.strip('[]'))
    return personalities