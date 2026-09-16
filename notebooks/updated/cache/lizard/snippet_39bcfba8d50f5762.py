def automeshgrid(x, y, step=0.02, xstep=None, ystep=None, pad=0.5, xpad=
    None, ypad=None):
    if xpad is None:
        xpad = pad
    if xstep is None:
        xstep = step
    if ypad is None:
        ypad = pad
    if ystep is None:
        ystep = step
    xmin = x.min() - xpad
    xmax = x.max() + xpad
    ymin = y.min() - ypad
    ymax = y.max() + ypad
    return meshgrid(xmin, xmax, step, ymin, ymax, ystep)