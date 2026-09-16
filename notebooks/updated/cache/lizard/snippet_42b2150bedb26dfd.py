def _cast_to_type(self, value):
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, datetime.date):
        return value
    try:
        value = date_parser(value)
        return value.date()
    except ValueError:
        self.fail('invalid', value=value)