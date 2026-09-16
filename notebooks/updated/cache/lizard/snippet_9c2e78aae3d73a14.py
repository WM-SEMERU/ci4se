def auto_zoom(zoomx=True, zoomy=True, axes='gca', x_space=0.04, y_space=
    0.04, draw=True):
    _pylab.ioff()
    if axes == 'gca':
        axes = _pylab.gca()
    x10, x20 = axes.get_xlim()
    y10, y20 = axes.get_ylim()
    axes.autoscale(enable=True, tight=True)
    if axes.get_xscale() == 'linear':
        x1, x2 = axes.get_xlim()
        xc = 0.5 * (x1 + x2)
        xs = 0.5 * (1 + x_space) * (x2 - x1)
        axes.set_xlim(xc - xs, xc + xs)
    if axes.get_yscale() == 'linear':
        y1, y2 = axes.get_ylim()
        yc = 0.5 * (y1 + y2)
        ys = 0.5 * (1 + y_space) * (y2 - y1)
        axes.set_ylim(yc - ys, yc + ys)
    if not zoomx:
        axes.set_xlim(x10, x20)
    if not zoomy:
        axes.set_ylim(y10, y20)
    if draw:
        _pylab.ion()
        _pylab.draw()