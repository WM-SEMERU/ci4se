def get(self, varname, idx=0, units=None):
    if not varname in self.mapping.vars:
        raise fgFDMError('Unknown variable %s' % varname)
    if idx >= self.mapping.vars[varname].arraylength:
        raise fgFDMError(
            'index of %s beyond end of array idx=%u arraylength=%u' % (
            varname, idx, self.mapping.vars[varname].arraylength))
    value = self.values[self.mapping.vars[varname].index + idx]
    if units:
        value = self.convert(value, self.mapping.vars[varname].units, units)
    return value