def hist(darray, figsize=None, size=None, aspect=None, ax=None, **kwargs):
    ax = get_axis(figsize, size, aspect, ax)
    xincrease = kwargs.pop('xincrease', None)
    yincrease = kwargs.pop('yincrease', None)
    xscale = kwargs.pop('xscale', None)
    yscale = kwargs.pop('yscale', None)
    xticks = kwargs.pop('xticks', None)
    yticks = kwargs.pop('yticks', None)
    xlim = kwargs.pop('xlim', None)
    ylim = kwargs.pop('ylim', None)
    no_nan = np.ravel(darray.values)
    no_nan = no_nan[pd.notnull(no_nan)]
    primitive = ax.hist(no_nan, **kwargs)
    ax.set_title('Histogram')
    ax.set_xlabel(label_from_attrs(darray))
    _update_axes(ax, xincrease, yincrease, xscale, yscale, xticks, yticks,
        xlim, ylim)
    return primitive