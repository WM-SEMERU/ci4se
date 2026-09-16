def escape_header(val):
    if val is None:
        return None
    try:
        return quote(val, encoding='ascii', safe='/ ')
    except ValueError:
        return "utf-8''" + quote(val, encoding='utf-8', safe='/ ')