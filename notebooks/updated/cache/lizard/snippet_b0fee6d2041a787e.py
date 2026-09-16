def validate_regex(ctx, param, value):
    if not value:
        return None
    try:
        re.compile(value)
    except re.error:
        raise click.BadParameter('Invalid regex "{0}" provided'.format(value))
    return value