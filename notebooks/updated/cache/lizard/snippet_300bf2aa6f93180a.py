def lex(code, lexer):
    try:
        return lexer.get_tokens(code)
    except TypeError as err:
        if isinstance(err.args[0], str) and ('unbound method get_tokens' in
            err.args[0] or 'missing 1 required positional argument' in err.
            args[0]):
            raise TypeError(
                'lex() argument must be a lexer instance, not a class')
        raise