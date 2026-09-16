def lag_plot(series, lag=1, ax=None, **kwds):
    import matplotlib.pyplot as plt
    kwds.setdefault('c', plt.rcParams['patch.facecolor'])
    data = series.values
    y1 = data[:-lag]
    y2 = data[lag:]
    if ax is None:
        ax = plt.gca()
    ax.set_xlabel('y(t)')
    ax.set_ylabel('y(t + {lag})'.format(lag=lag))
    ax.scatter(y1, y2, **kwds)
    return ax