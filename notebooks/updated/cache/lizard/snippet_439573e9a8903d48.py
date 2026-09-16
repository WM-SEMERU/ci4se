def fromtimestamp(cls, ts, tzi=None):
    if tzi is None:
        tzi = MinutesFromUTC(cls.get_local_utcoffset())
    return cls(datetime.fromtimestamp(ts, tzi))