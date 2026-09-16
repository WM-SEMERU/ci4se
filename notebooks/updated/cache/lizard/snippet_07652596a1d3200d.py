def multiplot(self, f, lfilter=None, plot_xy=False, **kargs):
    f = lambda_tuple_converter(f)
    lfilter = lambda_tuple_converter(lfilter)
    if lfilter is None:
        lst_pkts = (f(*e) for e in self.res)
    else:
        lst_pkts = (f(*e) for e in self.res if lfilter(*e))
    d = {}
    for k, v in lst_pkts:
        d.setdefault(k, []).append(v)
    if not kargs:
        kargs = MATPLOTLIB_DEFAULT_PLOT_KARGS
    if plot_xy:
        lines = [plt.plot(*zip(*pl), **dict(kargs, label=k)) for k, pl in
            six.iteritems(d)]
    else:
        lines = [plt.plot(pl, **dict(kargs, label=k)) for k, pl in six.
            iteritems(d)]
    plt.legend(loc='center right', bbox_to_anchor=(1.5, 0.5))
    if not MATPLOTLIB_INLINED:
        plt.show()
    return lines