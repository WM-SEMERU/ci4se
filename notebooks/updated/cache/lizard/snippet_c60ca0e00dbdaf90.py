def set(self, varname, value, idx=0, units=None):
    if not varname in self.mapping.vars:
        raise fgFDMError('Unknown variable %s' % varname)
    if idx >= self.mapping.vars[varname].arraylength:
        raise fgFDMError(
            'index of %s beyond end of array idx=%u arraylength=%u' % (
            varname, idx, self.mapping.vars[varname].arraylength))
    if units:
        value = self.convert(value, units, self.mapping.vars[varname].units)
    if math.isinf(value) or math.isnan(value) or math.fabs(value) > 3.4e+38:
        value = 0
    self.values[self.mapping.vars[varname].index + idx] = value