def date_from_string(string, format_string=None):
    if isinstance(format_string, str):
        return datetime.datetime.strptime(string, format_string).date()
    elif format_string is None:
        format_string = ['%Y-%m-%d', '%m-%d-%Y', '%m/%d/%Y', '%d/%m/%Y']
    for format in format_string:
        try:
            return datetime.datetime.strptime(string, format).date()
        except ValueError:
            continue
    raise ValueError('Could not produce date from string: {}'.format(string))