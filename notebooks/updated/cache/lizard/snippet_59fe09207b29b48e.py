def parse_date(date, default=None):
    if date == '':
        if default is not None:
            return default
        else:
            raise Exception('Unknown format for ' + date)
    for format_type in ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M',
        '%Y-%m-%d %H', '%Y-%m-%d', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M',
        '%d/%m/%Y %H', '%d/%m/%Y']:
        try:
            return datetime.strptime(date, format_type)
        except ValueError:
            pass
    raise Exception('Unknown format for ' + date)