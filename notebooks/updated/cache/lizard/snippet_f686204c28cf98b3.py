def fromstring(cls, isostring):
    if isinstance(isostring, basestring) and len(isostring) == 7 and isostring[
        4] == 'W':
        return cls(int(isostring[0:4]), int(isostring[5:7]))
    elif isinstance(isostring, basestring) and len(isostring
        ) == 8 and isostring[4:6] == '-W':
        return cls(int(isostring[0:4]), int(isostring[6:8]))
    else:
        raise ValueError(
            'Week.tostring argument must be on the form <yyyy>W<ww>; got %r' %
            (isostring,))