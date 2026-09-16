def make_tokens(parse_buffer):
    tokens = []
    for token_type, result in parse_buffer:
        token = token_type(result)
        if token is not None:
            tokens.append(token)
    return tokens