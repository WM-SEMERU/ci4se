def _get_matplot_dict(self, option, prop, defdict):
    cargs = self.curargs[option]
    result = cargs.copy()
    for varname in cargs:
        if prop in cargs[varname]:
            name = cargs[varname][prop]
            for key, val in list(defdict.items()):
                if val == name:
                    cargs[varname][prop] = key
                    break
    return result