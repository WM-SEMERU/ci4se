def do_dep(self, args):
    vals = args.split()
    twin = None
    if len(vals) > 1:
        if len(vals) == 2:
            var, plot = vals
        elif len(vals) == 3:
            var, plot, twin = vals
    else:
        var = vals[0]
        plot = None
    if not self._validate_var(var):
        msg.err(
            'Variable {} is not a valid file name and property combination.'
            .format(var))
    else:
        if var in self.curargs['dependents']:
            self.curargs['dependents'].remove(var)
        self.curargs['dependents'].append(var)
        if plot is not None:
            self.curargs['plottypes'][var] = plot
        if twin is not None:
            self.curargs['twinplots'][var] = twin