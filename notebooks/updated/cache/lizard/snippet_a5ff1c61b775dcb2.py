def _get_type(self):
    point = self._point
    typ = point.type
    bType = None
    if point.smooth:
        if typ == 'curve':
            bType = 'curve'
        elif typ == 'line':
            nextSegment = self._nextSegment
            if nextSegment is not None and nextSegment.type == 'curve':
                bType = 'curve'
            else:
                bType = 'corner'
    elif typ in ('move', 'line', 'curve'):
        bType = 'corner'
    if bType is None:
        raise FontPartsError('A %s point can not be converted to a bPoint.' %
            typ)
    return bType