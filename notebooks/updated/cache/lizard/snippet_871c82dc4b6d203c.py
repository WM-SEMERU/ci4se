def _evalUnits(self, datetimeString, sourceTime):
    s = datetimeString.strip()
    sourceTime = self._evalDT(datetimeString, sourceTime)
    modifier = ''
    m = self.ptc.CRE_UNITS.search(s)
    if m is not None:
        units = m.group('units')
        quantity = s[:m.start('units')]
    sourceTime = self._buildTime(sourceTime, quantity, modifier, units)
    return sourceTime