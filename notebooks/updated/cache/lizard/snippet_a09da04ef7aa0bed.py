def before(point):
    if not point:
        return True
    if isinstance(point, six.string_types):
        point = str_to_time(point)
    elif isinstance(point, int):
        point = time.gmtime(point)
    return time.gmtime() <= point