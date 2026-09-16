def validate_digit(value, start, end):
    if not str(value).isdigit() or int(value) < start or int(value) > end:
        raise ValueError('%s must be a digit from %s to %s' % (value, start,
            end))