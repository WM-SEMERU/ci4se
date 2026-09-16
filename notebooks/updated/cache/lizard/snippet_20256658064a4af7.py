def fromfile(cls, fileobj, coltype=LIGOTimeGPS):
    c = [cls.entry_class(line, coltype=coltype) for line in fileobj]
    return cls(c)