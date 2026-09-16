def x_frame2D(X, plot_limits=None, resolution=None):
    assert X.shape[1] == 2, 'x_frame2D is defined for two-dimensional inputs'
    if plot_limits is None:
        xmin, xmax = X.min(0), X.max(0)
        xmin, xmax = xmin - 0.075 * (xmax - xmin), xmax + 0.075 * (xmax - xmin)
    elif len(plot_limits) == 2:
        xmin, xmax = plot_limits
        try:
            xmin = xmin[0], xmin[1]
        except:
            xmin = [plot_limits[0], plot_limits[0]]
            xmax = [plot_limits[1], plot_limits[1]]
    elif len(plot_limits) == 4:
        xmin, xmax = (plot_limits[0], plot_limits[2]), (plot_limits[1],
            plot_limits[3])
    else:
        raise ValueError('Bad limits for plotting')
    resolution = resolution or 50
    xx, yy = np.mgrid[xmin[0]:xmax[0]:1.0j * resolution, xmin[1]:xmax[1]:
        1.0j * resolution]
    Xnew = np.c_[xx.flat, yy.flat]
    return Xnew, xx, yy, xmin, xmax