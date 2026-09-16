def get_field(ctx, field):
    if isinstance(field, str):
        field = getattr(ctx, field, None)
    if callable(field):
        field = field()
    elif isinstance(field, CommonToken):
        field = next(filter(lambda c: getattr(c, 'symbol', None) is field,
            ctx.children))
    return field