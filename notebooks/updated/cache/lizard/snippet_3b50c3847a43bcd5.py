def _zom_arg(lexer):
    tok = next(lexer)
    if isinstance(tok, COMMA):
        return (_expr(lexer),) + _zom_arg(lexer)
    else:
        lexer.unpop_token(tok)
        return tuple()