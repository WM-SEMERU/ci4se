def parse_definition_expr(expr, default_value=None):
    try:
        define, value = expr.split('=', 1)
        try:
            value = parse_number_token(value)
        except ValueError:
            value = parse_bool_token(value)
    except ValueError:
        if expr:
            define, value = expr, default_value
        else:
            raise ValueError('Invalid definition expression `%s`' % str(expr))
    d = define.strip()
    if d:
        return d, value
    else:
        raise ValueError('Invalid definition symbol `%s`' % str(define))