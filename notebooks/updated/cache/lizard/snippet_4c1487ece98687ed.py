def loadtxt(fn, **kwargs):
    global PP
    PP = PatternPull(fn)
    txtargs = PP.loadtxtargs()
    txtargs.update(kwargs)
    return np.loadtxt(fn, **txtargs)