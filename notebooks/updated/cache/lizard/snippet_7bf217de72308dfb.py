def axes(self):
    ret = utils.DefaultOrderedDict(lambda : self[1:0])
    for arr in self:
        if arr.psy.plotter is not None:
            ret[arr.psy.plotter.ax].append(arr)
    return OrderedDict(ret)