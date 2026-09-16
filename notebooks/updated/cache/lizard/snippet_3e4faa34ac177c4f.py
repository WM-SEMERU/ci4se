def match_token(token, tok_type, tok_str=None):
    return token.type == tok_type and (tok_str is None or token.string ==
        tok_str)