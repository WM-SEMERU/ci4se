def stack_hist(ax, stacked_data, sty_cycle, bottoms=None, hist_func=None,
    labels=None, plot_func=None, plot_kwargs=None):
    if hist_func is None:
        hist_func = np.histogram
    if plot_func is None:
        plot_func = filled_hist
    if plot_kwargs is None:
        plot_kwargs = {}
    print(plot_kwargs)
    try:
        l_keys = stacked_data.keys()
        label_data = True
        if labels is None:
            labels = l_keys
    except AttributeError:
        label_data = False
        if labels is None:
            labels = itertools.repeat(None)
    if label_data:
        loop_iter = enumerate((stacked_data[lab], lab, s) for lab, s in zip
            (labels, sty_cycle))
    else:
        loop_iter = enumerate(zip(stacked_data, labels, sty_cycle))
    arts = {}
    for j, (data, label, sty) in loop_iter:
        if label is None:
            label = 'dflt set {n}'.format(n=j)
        label = sty.pop('label', label)
        vals, edges = hist_func(data)
        if bottoms is None:
            bottoms = np.zeros_like(vals)
        top = bottoms + vals
        print(sty)
        sty.update(plot_kwargs)
        print(sty)
        ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **sty)
        bottoms = top
        arts[label] = ret
    ax.legend(fontsize=10)
    return arts