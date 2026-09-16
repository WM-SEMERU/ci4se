def year(columns, name=None):
    if columns < 0:
        raise BaseException()
    field = numeric(columns, name)
    field.addParseAction(_to_year)
    return field