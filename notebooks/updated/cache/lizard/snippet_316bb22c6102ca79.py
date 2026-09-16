def expect_token(token, tok_type, tok_str=None):
    if not match_token(token, tok_type, tok_str):
        raise ValueError('Expected token %s, got %s on line %s col %s' % (
            token_repr(tok_type, tok_str), str(token), token.start[0], 
            token.start[1] + 1))