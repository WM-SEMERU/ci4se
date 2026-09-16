def truncatechars(value, num, end_text='...'):
    length = None
    try:
        length = int(num)
    except ValueError:
        pass
    if length is not None and len(value) > length:
        return value[:length - len(end_text)] + end_text
    return value