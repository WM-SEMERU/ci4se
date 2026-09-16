def __force_datetime(self, obj):
    if isinstance(obj, datetime.datetime):
        return obj
    t = datetime.time(0, 0)
    return datetime.datetime.combine(obj, t)